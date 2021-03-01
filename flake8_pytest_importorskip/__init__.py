__version__ = '1.1.0'

from typing import Any, Dict, Iterator, Optional, Tuple, Type, cast


class PluginMeta(type):
    agency = None

    def __new__(
        cls: Type["PluginMeta"],
        clsname: str,
        superclasses: Tuple[type],
        attributedict: Dict[str, Any],
    ) -> "PluginMeta":
        if not cls.agency:
            cls.spy_on_pycodestyle()
        return cast(PluginMeta, type.__new__(cls, clsname, superclasses, attributedict))

    @classmethod
    def _interesting_line(cls, line: str) -> bool:
        # This misses `from pytest import importorskip`. PR welcome
        return "pytest.importorskip(" in line

    @classmethod
    def spy_on_pycodestyle(cls) -> None:
        import inspect

        import pycodestyle
        from kgb import SpyAgency

        cls.agency = SpyAgency()

        sig = inspect.signature(pycodestyle.module_imports_on_top_of_file)
        logical_line_idx = tuple(sig.parameters).index("logical_line")

        del sig

        @cls.agency.spy_for(pycodestyle.module_imports_on_top_of_file)
        def intercept_module_imports_on_top_of_file(  # pylint: disable=unused-variable
            *args: Any,
            **kwargs: Any,
        ) -> Optional[Iterator[Any]]:
            logical_line = args[logical_line_idx]

            if cls._interesting_line(logical_line):
                return None

            return pycodestyle.module_imports_on_top_of_file.call_original(
                *args, **kwargs
            )


class Plugin(metaclass=PluginMeta):
    name = __name__
    version = __version__

    def __init__(self, logical_line: str):
        pass

    def __iter__(self) -> Iterator[Any]:
        return self

    def __next__(self) -> Any:
        raise StopIteration()
