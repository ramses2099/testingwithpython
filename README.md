# Testing with python and pytest
Example of testing with pytest and python

# Create new branch in git
1. git checkout -b develop
1. git push origin develop
1. git branch --set-upstream-to=origin/develop develop
1. git branch

# Create virtual env
1. virtualenv env
1. active virtual env
1. source ./env/bin/activate
1. pip list
1. pip install --upgrade pip
1. pip install pytest

# Add conftest file 'conftest.py'
1. pytest_plugins = ['MODULE NAME']
1. create folter tests
1. add file test_module_name.py
1. run command pytest .