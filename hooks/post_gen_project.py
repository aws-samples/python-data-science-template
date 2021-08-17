import sys
from pathlib import Path

# missing_ok available only since python-3.8
# https://docs.python.org/3/library/pathlib.html#pathlib.Path.unlink
if sys.version_info[0:2] >= (3, 8):

    def rm(s: Path) -> None:
        Path(s).unlink(missing_ok=True)


else:

    def rm(s: Path) -> None:
        try:
            Path(s).unlink()
        except FileNotFoundError:
            pass


package_name = "{{cookiecutter.package_name}}".strip()
if package_name == "":
    # This project does not contain a Python package, hence, remove setup.py.
    rm("setup.py")
else:
    pkg_dir = Path("src") / package_name
    pkg_dir.mkdir()
    (pkg_dir / "__init__.py").touch()

license = "{{cookiecutter.open_source_license}}"
if license == "No license file":
    rm("LICENSE")

# Display next steps.
message = [
    "#" * 80,
    "# Congratulations, your project has been initialized!",
    "#",
    "# Recommended next steps:",
    "# - git init (this is needed for the ipython_config.py magic to work)",
    "# - pre-commit autoupdate",
    "# - pre-commit install",
    "# - review README.md",
]
if license != "No license file":
    message.append("# - review LICENSE")
if package_name != "":
    message += [
        "# - review and update setup.py, then remove the exception at the end.",
        "# - consider to adopt versioneer to version your package.",
    ]
message += [
    "# - git add .",
    "# - git commit",
    "#" * 80,
]
print(*message, sep="\n")
