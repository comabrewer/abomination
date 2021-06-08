import pytest

import abomination


def test_sadface():
    code = "\n".join([
        "def foo(",
        "):",
        "    pass",
    ])
    with pytest.raises(SyntaxError):
        abomination.call_out(code=code)


def test_no_sadface():
    code = "\n".join([
        "def foo():",
        "    pass",
    ])
    abomination.call_out(code=code)


def test_file(tmp_path):
    file = tmp_path / "code.py"
    code = "\n".join([
        "def foo(",
        "):",
        "    pass",
    ])
    file.write_text(code)
    with pytest.raises(SyntaxError):
        abomination.call_out(file=file)
