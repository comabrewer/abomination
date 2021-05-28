"""Test magic import."""
import subprocess
import venv

import pytest


@pytest.fixture
def python(tmp_path):
    """Create fresh venv and return path to python interpreter."""
    venv_dir = tmp_path / ".venv"
    venv.create(venv_dir, clear=True, with_pip=True)
    python = venv_dir / "bin" / "python"
    if not python.exists():
        python = venv_dir / "Scripts" / "python.exe"

    script = tmp_path / "script.py"

    def run(code):
        subprocess.run([python, "-m", "pip", "install", "."], check=True)
        script.write_text(
            f"import abomination; abomination.magic(); {code}"
        )
        subprocess.run([python, script], check=True)

    return run


def test_package_installable(python):
    python("import rich")


def test_package_installed(python):
    python("import setuptools")


def test_package_not_exists(python):
    with pytest.raises(subprocess.CalledProcessError):
        python("import zitti_e_buoni")
