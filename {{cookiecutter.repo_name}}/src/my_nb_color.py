"""Convenience module to setup color prints and logs in a Jupyter notebook.

Dependencies: `loguru`, `rich`.

Basic usage by an ``.ipynb``:

    >>> # Colorize notebook outputs
    >>> from my_nb_color import print, rprint, oprint
    >>>
    >>> # Test-drive different behavior of print functionalities
    >>> d = {"A" * 200, "B" * 200}
    >>> print("Colored:", d)
    >>> rprint("Colored and wrapped:", d)
    >>> oprint("Plain (i.e., Python's original):", d)
    >>> d  # Or: display(d)
    >>>
    >>> # Test-drive loguru
    >>> from loguru import logger
    >>> for f in (logger.debug, logger.info, logger.success, logger.error):
    >>>     f("Hello World!")


Robust usage by an ``.ipynb``, typically when the notebook file needs to run in an environment where
colors are not desired or dependencies are not installed:

    >>> # Best-effort to colorize notebook outputs
    >>> try:
    >>>     from my_nb_color import print, rprint, oprint
    >>> except ModuleNotFoundError:
    >>>     pass
    >>>
    >>> # Test-drive different behavior of print functionalities
    >>> d = {"A" * 200, "B" * 200}
    >>> print("Colored:", d)
    >>> rprint("Colored and wrapped:", d)
    >>> oprint("Plain (i.e., Python's original):", d)
    >>> d  # Or: display(d)
"""
# Try to setup rich.
try:
    import rich
except ModuleNotFoundError:
    print = rprint = oprint = print
else:
    oprint = print  # In-case needed

    rich.reconfigure(force_terminal=True, force_jupyter=False)
    rich.pretty.install()
    print = rich.get_console().out
    rprint = rich.get_console().print


# Try to setup loguru.
try:
    from loguru import logger
except ModuleNotFoundError:
    pass
else:
    try:
        get_ipython()
    except NameError:
        colorize = None
    else:
        colorize = True

    import sys

    logger.configure(handlers=[dict(sink=sys.stderr, colorize=colorize)])
    del colorize
