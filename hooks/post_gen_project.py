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
    rm("MANIFEST.in")
    rm("requirements/requirements-build.txt")
else:
    pkg_dir = Path("src") / package_name
    pkg_dir.mkdir()
    (pkg_dir / "__init__.py").touch()
    (pkg_dir / "py.typed").touch()

license = "{{cookiecutter.open_source_license}}"
if license == "No license file":
    rm("LICENSE")

# fmt: off
pre_commit = "{{cookiecutter.pre_commit}}"
if pre_commit != "advanced":
    rm(".gitleaks.toml")

# Display next steps.
cwd = Path().resolve()
message = [
    "#" * 80,
    "# Congratulations, your project has been initialized!",
    "#",
    f"# The generated project is located at {cwd}",
    "#",
    "# Recommended next steps:",
    f"# - cd {cwd}",
    "# - git init",
    "# - pre-commit autoupdate",
    "# - pre-commit install",
    "# - review README.md",
]
if license != "No license file":
    message.append("# - review LICENSE")
if package_name != "":
    message += [
        "# - review and update setup.py, then remove the exception at the start.",
    ]
message += [
    "# - git add .",
    "# - git commit",
    "#" * 80,
]
print(*message, sep="\n")
