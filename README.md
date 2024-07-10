# testingwithpython
Example of testing with pytest and python


# create new branch in git
## git checkout -b develop
## git push origin develop
## git branch --set-upstream-to=origin/develop develop

# list branch in git local
## git branch

# create virtual env
## virtualenv env
## active virtual env
### source ./env/bin/activate
### pip list
### pip install --upgrade pip
### pip install pytest

# add conftest file 'conftest.py'
## pytest_plugins = ['MODULE NAME']

# create folter tests
## add file test_module_name.py
## run command pytest .