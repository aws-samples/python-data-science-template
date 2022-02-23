"""Convenience module to setup color prints and logs in a Jupyter notebook.

Dependencies: `loguru`, `rich`.

Basic usage by an ``.ipynb``:

    >>> # Colorize notebook outputs
    >>> from my_nb_color import print, pprint, oprint
    >>>
    >>> # Test-drive different behavior of print functionalities
    >>> d = {"A" * 200, "B" * 200}
    >>> print("Colored:", d)
    >>> pprint("Colored and wrapped:", d)
    >>> oprint("Plain (i.e., Python's original):", d)
    >>> display(d)
    >>>
    >>> # Test-drive loguru
    >>> from loguru import logger
    >>> for f in (logger.debug, logger.info, logger.success, logger.error):
    >>>     f("Hello World!")
"""
import sys
from typing import Callable, cast

# Try to setup rich.
try:
    import rich
except ModuleNotFoundError:
    print = pprint = oprint = print
else:
    oprint = print  # In-case plain old behavior is needed
    rich.reconfigure(force_terminal=True)
    rich.pretty.install()

    _console = rich.console.Console(force_terminal=True, force_jupyter=False)
    print = cast(Callable, _console.out)
    _pprint = _console.print

    def pprint(*args, **kwargs):
        kwargs["soft_wrap"] = True
        _pprint(*args, **kwargs)

    def inspect(*args, **kwargs):
        if "console" not in kwargs:
            kwargs["console"] = _console
        rich.inspect(*args, **kwargs)

# Try to setup loguru.
try:
    from loguru import logger
except ModuleNotFoundError:
    pass
else:
    logger.configure(handlers=[dict(sink=sys.stderr, colorize=True)])
