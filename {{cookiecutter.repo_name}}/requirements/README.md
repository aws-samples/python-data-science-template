# Requirements Files

| File                     | Description                                   |
| ------------------------ | --------------------------------------------- |
| `requirements.txt`       | Mandatory requirement                         |
| `requirements-test.txt`  | Required for unit tests                       |
| `requirements-docs.txt`  | Required to generate the html documentations. |
{%- if cookiecutter.package_name != "" %}
| `requirements-build.txt` | Required to build the wheel.                  |
{%- endif %}
| `requirements-dev.txt`   | Recommended packages during development.      |
