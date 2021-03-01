import pytest


@pytest.fixture(name='plugin_config')
def _plugin_config(flake8dir, pytestconfig):
    flake8dir.make_setup_cfg(
        f"""\
            [flake8:local-plugins]
            extension =
              PYTESTIMPORTSKIP = flake8_pytest_importorskip:Plugin
            paths =
              {pytestconfig.rootdir}
            """
    )


def test_baseline(flake8dir):
    """
    Ensure that pycodestle reports the E402 still.

    This makes sure our plugin is actually silencing the error
    """
    flake8dir.make_example_py(
        """\
        a = 1

        import os

        os.exit(1)
        """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == [
        "./example.py:3:1: E402 module level import not at top of file",
    ]


@pytest.mark.usefixtures('plugin_config')
def test_importorskip_not_error(flake8dir):
    flake8dir.make_example_py(
        """\
        import sys

        import pytest

        pytest.importorskip("a")
        B = pytest.importorskip("a").B

        import os

        os.exit(1)
        sys.path
        """
    )
    result = flake8dir.run_flake8(["--ignore", "I900"])
    assert result.out_lines == []


@pytest.mark.usefixtures('plugin_config')
def test_other_toplevel_code_still_errors(flake8dir):
    flake8dir.make_example_py(
        """\
        import pytest

        a = 1

        pytest.importorskip("a")

        import os

        os.exit(1)
        """
    )
    result = flake8dir.run_flake8(["--ignore", "I900"])
    assert result.out_lines == [
        "./example.py:7:1: E402 module level import not at top of file"
    ]
