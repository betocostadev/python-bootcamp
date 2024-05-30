# Python - Learning about Packages
# Managing packages

print("\n======== Python - Learning about Packages ========\n")
print("======== Managing packages ========")

print(
    """
Some information about package managers like:
- pip
- pipenv
- poetry
"""
)

# Packages are a way to organize Python modules
# They are directories with a special __init__.py file
# This file can be empty, but it indicates that the directory is a Python package

# To avoid package version conflicts and to manage dependencies, it is recommended to use a virtual environment

# To create an use a virtual environment:
# python3 -m venv .env
# source .env/bin/activate
# pip install package_name

# To deactivate the virtual environment:
# deactivate

# To install a package:
# pip install package_name

# Other package managers for Python:
# conda
# pipenv
# poetry


# Some package managers like pipenv are good for managing dependencies and virtual environments
# They can help to delete unused packages and to keep track of the dependencies

# To install pipenv:
# pip install pipenv

# To create a virtual environment with pipenv:
# pipenv install package_name

# To activate the virtual environment:
# pipenv shell

# To deactivate the virtual environment:
# exit

# Pipenv creates a Pipfile and a Pipfile.lock to keep track of the dependencies

# Poetry is another package manager for Python

# To install poetry:
# pip install poetry

# To create a new project with poetry:
# poetry new project_name

# It's also possible to initialize a new project in an existing directory:
# poetry init

# To add a package to the project:
# poetry add package_name

# To install the dependencies:
# poetry install

# To run a script:
# poetry run python script.py

# Poetry creates a pyproject.toml file to keep track of the dependencies
