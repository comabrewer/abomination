# abomination

*A dumpster fire of metaprogramming and other Python abuses.*

Some code is so bad it just has to be written, documented, tested, and packaged.
This is the place for such ideas.

## Installation

Install the package from pypi:

```sh
pip install abomination
```

## Usage

### Automatic installation of packages

Somewhere before your first third-party import, but the following line:

```py
import abomination; abomination.magic()
```

If an import fails, we will try to install the package with pip and restart the
script.

```py
import abomination; abomination.magic()

# This just works!
import numpy as np
```

Of course, this only works if the import name matches the distribution name.
Prepare for an ugly recursion while Python screams "I cannot import `pyyaml`!"
and pip shouts back "But I have already installed `pyyaml`!"
(note: the import name is `yaml`).

### Calling out code style you don't like

Linters are for the weak, *real* checks hit hard at run time!
Following the example of Python's treatment of whitespace,
code style violations raise a `SyntaxError` if you call `call_out`:

```py
import abomination

abomination.call_out(sadface=True)

# Some dummy code to provoke
if (
    this_code_uses_some_practices_that_i_dislike := True
    and others_should_know_about_it := True
):
    pass

```

Output:
```
SyntaxError: It saddens me to see '):' in your code :(
```

> This function, just like the whole package, is intended as a light-hearted joke.
> It was inspired by this twitter thread: https://twitter.com/gvanrossum/status/1395135889123069952
> If anyone involved feels offended, please contact me and I will remove it.
