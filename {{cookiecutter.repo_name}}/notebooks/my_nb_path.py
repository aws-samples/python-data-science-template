"""Allow notebooks to import custom modules at a few pre-defined places within this project's
git repository.

When imported, adds ``GITROOT``, ``GITROOT/src/``, and ``GITROOT/notebooks`` to `sys.path`.

Place this file in the same directory as your ``.ipynb`` files. If ``.ipynb`` files are organized
into subfolders, please ensure this file is presented in each subfolder. Example:

.. code-block:: bash

    GITROOT
    |-- .git                   # GITROOT/ must be a git repository
    |-- notebooks              # Jupyter notebooks
    |   |-- folder-a
    |   |   |-- my_nb_path.py  # Importable by *.ipynb in this subfolder
    |   |   |-- nb-abc.ipynb
    |   |   `-- nb-xyz.ipynb
    |   |-- my_nb_path.py      # Importable by *.ipynb in this subfolder
    |   |-- nb-01.ipynb
    |   `-- nb-02.ipynb
    `-- src
        `-- my_custom_module
            |-- __init__.py
            `-- ...

Usage by ``.ipynb``:

.. code-block:: python

    # Allow this notebook to import from ``GITROOT/``, ``GITROOT/src/``, and
    # ``GITROOT/notebooks``.
    import my_nb_path

    # Test-drive importing a custom module under ``GITROOT/src/``.
    import my_custom_module

Background: we used to rely on ``ipython_config.py`` in the current working directory files.
However, IPython 8.0.1, 7.31.1 and 5.11 onwards disable this approach to prevent potential
Execution with Unnecessary Privileges, as described
[here](https://ipython.readthedocs.io/en/stable/whatsnew/version8.html#ipython-8-0-1-cve-2022-21699).

So now, each ``.ipynb`` must explicitly modify its own `sys.path`, and this module is provided for
convenience of writing such a logic.
"""
import os
import subprocess
import sys
from pathlib import Path
from typing import Union

def sys_path_append(o: Union[str, os.PathLike]) -> None:
    posix_path: str = o.as_posix() if isinstance(o, Path) else Path(o).as_posix()
    if posix_path not in sys.path:
        sys.path.insert(0, posix_path)

# Add GIT_ROOT/ and a few other subdirs
_p = subprocess.run(
    ["git", "rev-parse", "--show-toplevel"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
)

if _p.returncode == 0:
    _git_root: str = _p.stdout[:-1].decode("utf-8")  # Remove trailing '\n'
    _git_root_p = Path(_git_root)

    my_sys_paths = [
        _git_root_p,
        _git_root_p / "src",
        _git_root_p / "notebooks",
    ]
    for sp in my_sys_paths:
        sys_path_append(sp)
