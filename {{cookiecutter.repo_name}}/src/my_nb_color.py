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
import warnings
from typing import Callable, cast

# Try to setup rich.
try:  # noqa: C901
    import rich
except ModuleNotFoundError:
    print = pprint = oprint = print

    def inspect(*args, **kwargs):
        warnings.warn(f"{__name__}.inspect() requires rich.")

else:
    from rich.console import Console

    oprint = print  # In-case plain old behavior is needed
    _console = Console(force_terminal=True, force_jupyter=False)
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

    inspect = cast(Callable, Inspect())

    def opinionated_rich_pretty_install():
        """Intercept any post-ipython renderings.

        Known cases fixed (as of rich-11.2.0): (i) prevent pandas dataframe rendered twice (as text
        and as html), (ii) do not show ``<Figure ...>`` on matplotlib figures.
        """
        from IPython import get_ipython
        from IPython.core.formatters import BaseFormatter
        from rich import get_console
        from rich.abc import RichRenderable
        from rich.console import ConsoleRenderable
        from rich.pretty import Pretty, _safe_isinstance

        class MyRichFormatter(BaseFormatter):
            # Based on: rich.pretty.install._ipy_display_hook()
            # Customized behaviors are described in the comments.
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

            def __call__(self, value, *args, **kwargs):
                console = get_console()
                if console.is_jupyter:
                    for repr_name in self.reprs:
                        try:
                            repr_method = getattr(value, repr_name)
                            repr_result = repr_method()
                        except (
                            AttributeError,  # value object has does not have the repr attribute
                            Exception,  # any other error
                        ):
                            continue
                        else:
                            # Customized behavior: once rendered by ipython's repr, do no further.
                            if repr_result is not None:
                                return

                # Customized behavior: when None of the ipython repr work, output color ascii.
                console = Console(force_terminal=True, force_jupyter=False)
                # End of customized behavior

                # certain renderables should start on a new line
                if _safe_isinstance(value, ConsoleRenderable):
                    console.line()

                with console.capture() as capture:
                    console.print(
                        value
                        if _safe_isinstance(value, RichRenderable)
                        else Pretty(
                            value,
                            overflow="ignore",
                            indent_guides=False,
                            max_length=None,
                            max_string=None,
                            expand_all=False,
                            margin=12,
                        ),
                        crop=False,
                        new_line_start=True,
                    )
                return capture.get()

        rich.reconfigure(force_terminal=True)
        rich.pretty.install()
        ipy_formatters = get_ipython().display_formatter.formatters
        rich_formatter = ipy_formatters["text/plain"]
        if rich_formatter.__module__ == "rich.pretty":
            ipy_formatters["text/plain"] = MyRichFormatter()

    opinionated_rich_pretty_install()

# Try to setup loguru.
try:
    from loguru import logger
except ModuleNotFoundError:
    pass
else:
    logger.configure(handlers=[dict(sink=sys.stderr, colorize=True)])
