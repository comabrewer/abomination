"""A dumpster fire of metaprogramming and other Python abuses."""
import sys
import subprocess


def magic():
    """Try to install missing packages on failing import."""
    original_hook = sys.excepthook

    def excepthook(type, value, traceback):
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
