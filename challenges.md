### Challenges to resolve
- How to deploy python application on droplet with all the dependencies 
    Using pipenv
     - ` cd <projectname> `
     - `pipenv --python 3.6` sets up the project to be a virtual environment with dependecies managed by pipenv.
     - `pipenv shell` activates the virtual environment (must be done in terminal first thing every time) 
     - `pipenv install <packagename>` installs the python package into the virtual environment and writes it to the pipfile
     - `pipenv uninstall --all-dev <package name>` removes package both from env and from pipfile
     - `pipenv lock` creates a file: pipfile.lock to ensure deterministic builds (that all dependencies are exactly the right versions)
    - Using MySql with python
    `pipenv install mysql-connector-python-rf`  

### Modules in python
    - Create a subdirectory named lib.
    - Create an empty file named lib\__init__.py.
    - `from lib import <filename> as <alias>`

### Unit testing
    - `pipenv install pytest`
    - create a new file with name: test_<some name> 
    - inside create a function named: test_<some name>
    - inside it use assert expected == result
    - run it from terminal like: `python -m pytest` or `py.test` or `py.test -v` (v for verbose: see all details about the test runs when they fail) or `py.test -s` (-s will print all to console)
        - pytest will inspect all files and find those named 'test_* with functions named test_*
