# Dependencies
This project requires the following to run:

1. Python >= 3.7.10
2. Flask
3. Flask-Login
4. SQLAlchemy
5. Werkzeug
6. pytest

*While not a requirement, this installation guide assumes that the system is being installed on a Linux-based OS*

## Dependency Installation
1. Ensure python is installed and up to date through the use of the command `python3 --version` 
    1. If python is not installed, use the commands `sudo apt-get update` and `sudo apt-get install python3.7`
    2. While not required, it is best practice to install python modules through the use of pip, which can be installed through the command `python -m ensurepip --upgrade`
2. Once python 3.7 is installed, install the required modules as so:
    1. Flask: `python -m pip install Flask`
        1. Further documentation can be found at: https://flask.palletsprojects.com/en/2.0.x/installation/
    2. Flask-Login: `python -m pip install flask-login`
        1. Further documentation can be found at: https://flask-login.readthedocs.io/en/latest/
    3. SQLAlchemy: `python -m pip install SQLALchemy`
        1. Further documentation can be found at: https://docs.sqlalchemy.org/en/14/intro.html#installation
    4. Werkzeug: Is installed automaticall as part of Flask
    5. pytest: `python -m pip install pytest
        1. Further documentation can be found at: https://docs.pytest.org/en/7.0.x/

# Installation
Once all dependencies are installed, simply navigate to the root folder for the repository and use the command `python -m pytest`

Note: HTML files are currently just template ones taken from Internet, final versions will differ (and will be created to match designs)
