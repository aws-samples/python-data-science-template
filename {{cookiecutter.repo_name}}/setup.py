# raise ValueError(
#     "Baseline setup.py from cookiecutter aws-samples/python-data-science-template. "
#     "Please review and modify accordingly, then remove this exception"
# )

import os
from typing import List

from setuptools import find_packages, setup

_repo: str = "{{cookiecutter.repo_name}}"
_pkg: str = "{{cookiecutter.package_name}}"
_version = "0.0.1"


def read_lines(fname: str) -> List[str]:
    """Read the content of a file.

    You may use this to get the content of, for e.g., requirements.txt, VERSION, etc.
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).readlines()


def read_requirements(fname: str) -> List[str]:
    lines = [
        flip_git(stripped_line)
        for stripped_line in (line.strip() for line in read_lines(fname))
        if stripped_line != ""
    ]

    return lines


def flip_git(s: str) -> str:
    """Flip pip's git source from ``requirements.txt`` format to `setuptools` format.

    If `s` is not a git source, return as-is.

    Args:
        s (str): a line in ``requirements.txt``.

    Returns:
        str: if `s` is ``git+.://gh.com/a/b@c#egg=d``, then return ``d @ git+.://gh.com/a/b@c``.
        Otherwise, return as-is.
    """
    if not s.startswith("git+"):
        return s
    git_url, egg = s.rsplit("#", 1)
    _, egg_name = egg.split("=")
    return f"{egg_name} @ {git_url}"


# Declare minimal set for installation
required_packages: List[str] = read_requirements("requirements.txt")
extras = {
    "dev": read_requirements("requirements-dev.txt"),
    "test": read_requirements("requirements-test.txt"),
}

setup(
    name=_pkg,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    version=_version,
    description="{{cookiecutter.description}}",
    long_description=read("README.md"),
    author="{{cookiecutter.author_name}}",
    url=f"https://github.com/abcd/{_repo}/",
    download_url="",
    project_urls={
        "Bug Tracker": f"https://github.com/abcd/{_repo}/issues/",
        "Documentation": f"https://{_repo}.readthedocs.io/en/stable/",
        "Source Code": f"https://github.com/abcd/{_repo}/",
    },
    {% if cookiecutter.open_source_license != "No license file" -%}
    license="{{cookiecutter.open_source_license}}",
    {% endif -%}
    keywords="word1 word2 word3",
    platforms=["any"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        {% if cookiecutter.open_source_license != "No license file" -%}
        "License :: OSI Approved :: {{cookiecutter.open_source_license}}",
        {% endif -%}
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8.0",
    install_requires=required_packages,
    extras_require=extras,
)
