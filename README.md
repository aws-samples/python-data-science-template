# A cookiecutter template for Python data science projects

## Pre-requisite

You need to have the cli `cookiecutter` available in your Python environment.
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
|   `-- my_nb_path.py            # Imported by *.ipynb to treat src/ as PYTHONPATH
|-- setup.py                     # To pip install your Python module (if module name specified to cookiecutter)
|-- src
|   |-- my_custom_module         # Your custom module
|   |-- my_nb_color.py           # Imported by *.ipynb to colorize their outputs
|   `-- source_dir               # You can further create this subdir for SageMaker entrypoint scripts
|-- tests                        # Unit tests

# These sample configuration files are auto-generated too:
|-- .editorconfig                # Sample editor config (for IDE / editor that supports this)
|-- .gitattributes               # Sample .gitattributes
|-- .gitignore                   # Sample .gitignore
|-- .pre-commit-config.yaml      # Sample precommit hooks
|-- .vscenv                      # Sample dot env with PYTHONPATH config (for IDE /editor that supports this)
|-- LICENSE                      # Boilperplate (auto-generated content based on what you specified to cookiecutter)
|-- README.md                    # Template for you to customize
|-- pyproject.toml               # Sample setting for Python code formatter
`-- tox.ini                      # Sample configurations for Python toolchains
```

This structure has been used in a few other places as well, e.g.,
[aws-samples/sagemaker-rl-energy-storage-system](https://github.com/aws-samples/sagemaker-rl-energy-storage-system)
and [aws-samples/amazon-sagemaker-gluonts-entrypoint](https://github.com/aws-samples/amazon-sagemaker-gluonts-entrypoint).
Feel free to look at those repositories and observe the project structure
documented in their `README.md`.

## Related Projects

Ready to start your new data science project on AWS? If so, you may want to
check on these related samples.

1. Do you like to work on EC2 instances? Then why don't you check out these
   [simple template](https://github.com/aws-samples/ec2-data-science-vim-tmux-zsh/)
   to setup basic Vim, Tmux, Zsh for the Deep Learning AMI Amazon Linux 2 for
   data scientsts.

2. Do you like to work on SageMaker classic notebook instances? Then why don't you check out the
   [one-liner customization command](https://github.com/aws-samples/amazon-sagemaker-notebook-instance-customization)
   that quickly applies common tweaks on a fresh (i.e., newly created or
   rebooted) SageMaker classic notebook instance, to make the notebook instance
   a little bit more ergonomic for prolonged usage.

3. Are you loooking for a quickstart to accelerate the delivery of custom ML
   solutions to production, without having to make too many design choices? Then
   why don't you check out the [ML Max repo](https://github.com/awslabs/mlmax/)
   which includes templates for four pillars: training pipeline, inference
   pipeline, development environment and data management/ETL.

4. Are you tired of repeatedly writing the same boilerplate codes for common,
   tactical data science tasks? Then why don't you check on the
   [SageMaker meta-entrypoint utilities](https://github.com/aws-samples/amazon-sagemaker-entrypoint-utilities),
   and the [smallmatter library](https://github.com/aws-samples/smallmatter-package).

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
