from typing import Any, Dict

__version__ = '1.0.0.post0'


def patch_pytest_importorskip(
    logical_line: str,
    previous_logical: str,
    _checker_states: Dict[str, Any],
) -> Any:
    def _interesting_line(line: str) -> bool:
        # This misses `from pytest import importorskip`. PR welcome
        return "pytest.importorskip(" in line

    if "pycodestyle.module_imports_on_top_of_file" not in _checker_states:
        return ()

    if _interesting_line(logical_line) or _interesting_line(previous_logical):
        _checker_states["pycodestyle.module_imports_on_top_of_file"][
            "seen_non_imports"
        ] = False

    return ()


patch_pytest_importorskip.name = "PytestImportSkip"  # type: ignore
patch_pytest_importorskip.version = __version__  # type: ignore
