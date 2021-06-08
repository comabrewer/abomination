"""A dumpster fire of metaprogramming and other Python abuses."""
import re
import sys
import subprocess
from pathlib import Path
from typing import Union


def magic():
    """Try to install missing packages on failing import."""
    original_hook = sys.excepthook

    def excepthook(type, value, traceback):
        print(type, value, traceback)
        if type is not ModuleNotFoundError:
            original_hook(type, value, traceback)
            return
        module = value.args[0].split("'")[1]
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", module]
        )
        if result.returncode:
            raise RuntimeError(f"Could not install missing package '{module}'")

        # Let's try to run the script again
        result = subprocess.run([sys.executable, *sys.argv])
        sys.exit(result.returncode)

    sys.excepthook = excepthook


def call_out(
    file: Union[str, Path] = __file__,
    code: str = "",
    sadface: bool = True,
):
    """Call out bad coding practices.

    As a bad meta-joke, the signature of this function is intentionally
    written in the very code style it was meant to destroy.

    More checks may be added in the future.

    Args:
        file: Path to source file. Defaults to this file.
        code: String of Python code. If code is given, the file will be
            ignored.
        sadface: Whether to check for sadface line break style.

    Raises:
        SyntaxError if any style issue is encountered.

    """
    if not code:
        code = Path(file).read_text()

    if sadface and re.search(r"^\s*\):$", code, re.MULTILINE):
        raise SyntaxError("It saddens me to see '):' in your code :(")

