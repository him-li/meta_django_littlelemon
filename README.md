# meta_django_littlelemon
## Working with virtual environments on your local machine
Python uses venv as the preferred module to create and manage virtual environments. venv is also included in the Python standard library and does not require any additional installation.

venv (for Python 3) and virtualenv (for Python 2) allow you to manage separate package installations for different projects. 

In case you want to install virtualenv that is used for earlier versions of Python, use the command:

Windows: `py -m pip install --user virtualenv`

MacOS: `python3 -m pip install --user virtualenv`

You can create a virtual environment in the specific project directory by running a command:

Windows: `py -m venv env`

MacOS: `python3 -m venv env`

### Note:
```
env is the name assigned to the virtual environment and this will create a virtual Python installation in the env folder.
```
### Activate the virtual environment

Next you need to activate the virtual environment. You will put the virtual environment-specific python and pip executables into your shell’s PATH.

You can do this by running a command such as:

Windows: `.\env\Scripts\activate`

MacOS: `source env/bin/activate`
### Exit the virtual environment
You can exit the virtual environment by running the command:

MacOS and Windows: `deactivate`

There may be OS specific difficulties you may encounter while installing and using virtual environments.

More information can be found on the official Python website.

### Note:
```
venv is not the only option available for creating virtual environments and other options exist such as pipenv which is another variation.
```