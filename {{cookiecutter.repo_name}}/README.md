# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Project Structure

```text
{{cookiecutter.repo_name}}
|-- bin/                         # CLI scripts
|-- notebooks
|   |-- *.ipynb                  # Jupyter notebooks
|   `-- my_nb_path.py            # Imported by *.ipynb to treat src/ as PYTHONPATH
|-- requirements/                # Dependencies required by this project
|-- src                          # Python modules developed in this project
{% if cookiecutter.package_name != "" -%}
|   |-- {{cookiecutter.package_name}}
{% endif -%}
|   `-- my_nb_color.py           # Imported by *.ipynb to colorize their outputs
|-- tests/                       # Unit tests
{% if cookiecutter.package_name != "" -%}
|-- MANIFEST.in                  # Required by setup.py
|-- setup.py                     # To pip install {{cookiecutter.package_name}}
{% endif %}
# Miscellaneous files
|-- .editorconfig                # Editor config (for IDE / editor that support this)
|-- .gitattributes               # Files that Git must give special treatments
{% if cookiecutter.pre_commit == "advanced" -%}
|-- .gitleaks.toml               # Configuration for Gitleaks tool
{% endif -%}
|-- .gitignore                   # Git ignore list
|-- .pre-commit-config.yaml      # Precommit hooks
|-- LICENSE                      # License
|-- README.md                    # Template document
|-- pyproject.toml               # Settings for select Python toolchains
`-- tox.ini                      # Settings for select Python toolchains
```

## Credits

This project was initialized by {{cookiecutter.author_name}} using:

```bash
cookiecutter https://github.com/aws-samples/python-data-science-template
```

## License

This library is licensed under the {{cookiecutter.open_source_license}}.{% if cookiecutter.open_source_license != "No license file" %} See the [LICENSE](LICENSE) file.{%- endif %}
