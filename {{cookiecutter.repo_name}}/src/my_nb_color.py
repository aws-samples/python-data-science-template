"""Convenience module to setup color prints and logs in a Jupyter notebook.

Dependencies: `loguru`, `rich`.

Basic usage by an ``.ipynb``:

    >>> # Colorize notebook outputs
    >>> from my_nb_color import print, pprint, oprint, inspect
    >>>
    >>> # Test-drive different behavior of print functionalities
    >>> d = {"A" * 200, "B" * 200}
    >>> print("Colored:", d)
    >>> pprint("Colored and wrapped:", d)
    >>> oprint("Plain (i.e., Python's original):", d)
    >>> display(d)
    >>>
    >>> import pandas as pd
    >>> df = pd.DataFrame(dict(a=[1,2,3], b=[4,5,6]))
    >>> display(d, df)
    >>> df.plot();
    >>>
    >>> inspect(df)
    >>> inspect(print)
    >>> inspect(pprint)
    >>> inspect(inspect)
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

    rich.reconfigure(force_terminal=True, force_jupyter=False)
    _console = rich.get_console()

    print = cast(Callable, _console.out)

    def pprint(*args, soft_wrap=True, **kwargs):
        """Call ``rich.console.Console(...).print(..., soft_wrap=True, ...)``."""
        _console.print(*args, soft_wrap=soft_wrap, **kwargs)

    class Inspect:
        def __init__(self, console=_console):
            self.console = _console

        def __call__(self, obj, *args, **kwargs):
            """Call ``rich.inspect(..., console=<preset_console>, ...)``."""
            # Do not inspect wrappers, because *args & **kwargs are not useful for callers.
            #
            # Implementation notes: make sure the pattern is:
            #
            #   if <RHS> is <LHS>:
            #       <LHS> = <RHS>
            if self is obj:
                obj = rich.inspect
            elif pprint is obj:
                obj = self.console.print

            rich.inspect(obj, *args, console=self.console, **kwargs)

    inspect = Inspect()

    def opinionated_rich_pretty_install():
        """Intercept any post-ipython renderings.

        Known cases fixed (as of rich-11.2.0): (i) prevent pandas dataframe rendered twice (as text
        and as html), (ii) do not show ``<Figure ...>`` on matplotlib figures.
        """
        from IPython.core.formatters import BaseFormatter

        class RichFormatterWrapper(BaseFormatter):
            # See: rich.pretty.install._ipy_display_hook()
            reprs = [
                "_repr_html_",
                "_repr_markdown_",
                "_repr_json_",
                "_repr_latex_",
                "_repr_jpeg_",
                "_repr_png_",
                "_repr_svg_",
                "_repr_mimebundle_",
            ]

            def __init__(self, rich_formatter):
                self.rich_formatter = rich_formatter

            def __call__(self, value, *args, **kwargs):
                for repr_name in self.reprs:
                    try:
                        repr_method = getattr(value, repr_name)
                        repr_method()
                    except (
                        AttributeError,  # value object has does not have the repr attribute
                        Exception,  # any other error
                    ) as e:
                        continue
                    else:
                        return
                else:
                    # None of the ipython methods work, hence let rich takes over
                    self.rich_formatter(value, *args, **kwargs)

        rich.pretty.install()
        ipy_formatters = get_ipython().display_formatter.formatters
        rich_formatter = ipy_formatters["text/plain"]
        if rich_formatter.__module__ == "rich.pretty":
            ipy_formatters["text/plain"] = RichFormatterWrapper(rich_formatter)

    opinionated_rich_pretty_install()

# Try to setup loguru.
try:
    from loguru import logger
except ModuleNotFoundError:
    pass
else:
    logger.configure(handlers=[dict(sink=sys.stderr, colorize=True)])
