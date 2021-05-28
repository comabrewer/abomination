# abomination

*A dumpster fire of metaprogramming and other Python abuses.*

Some code is so bad it just has to be written, documented, test and packaged.
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
Prepare for an ugly recursion while Python screams "I cannot import `pyyaml`!" and pip shouts back "But I have already installed `pyyaml`!" (note: the import name is `yaml`).

