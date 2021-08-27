# A cookiecutter template for Python data science project

## Pre-requisite

You need to have the cli `cookiecutter` available on your Python environment.
Please see its installation instructions
[here](https://cookiecutter.readthedocs.io/en/latest/installation.html).

## Usage

To generate a directory structure for a new data science project, you can run
the following commands in your Python environment.

```bash
cookiecutter https://github.com/aws-samples/python-data-science-template
```

![setup-example-640px](https://user-images.githubusercontent.com/6405428/130512903-38e4fc96-e5b5-44f5-a4bd-4b4d4c6b3681.gif)

Alternatively, you can also clone this repository to use a local template:

```bash
# Clone to a local repository in the current directory.
git clone https://github.com/aws-samples/python-data-science-template.git

# The above command creates python-data-science-template/ in the current dir.

# Use the local repo to generate project structure
cookiecutter python-data-science-template
```

## Project Structure

By using this template, your data science project is auto-generated as follows:

```
.
|-- notebooks                    # A directory to place all notebooks files.
|   |-- *.ipynb
|   `-- ipython_config.py        # IPython magic to let *.ipynb treat src/ as PYTHONPATH
|-- setup.py                     # To pip install your Python module (if module name specified to cookiecutter)
|-- src
|   |-- my_custom_module         # A custom module
|   `-- source_dir               # SageMaker training job's source_dir and entrypoint script
|-- tests                        # Unit tests for SageMaker's ray launcher

# These sample configuration files are auto-generated too:
|-- .editorconfig                # Sample editor config (for IDE / editor that support this)
|-- .gitattributes               # Sample .gitattributes
|-- .gitignore                   # Sample .gitignore
|-- .pre-commit-config.yaml      # Sample precommit hooks
|-- .vscenv                      # Sample dot env with PYTHONPATH config (for IDE /editor that support this)
|-- LICENSE                      # Boilperplate (auto-generated content based on what specified to cookiecutter)
|-- README.md                    # Template for you to customize
|-- ipython_config.py            # Sample copy of ipython_config.py (same as notebook/ipython_config.py)
|-- pyproject.toml               # Sample setting for Python code formatter
`-- tox.ini                      # Sample configurations for Python toolchains
```

This structure has been used in a few other places as well, e.g.,
[aws-samples/sagemaker-rl-energy-storage-system](https://github.com/aws-samples/sagemaker-rl-energy-storage-system)
and [aws-samples/amazon-sagemaker-gluonts-entrypoint](https://github.com/aws-samples/amazon-sagemaker-gluonts-entrypoint).
Feel free to look at those repositories and observe the project structure
documented in their `README.md`.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
