# Physics Dictionary Web Interface

A web interface for searching the [physics dictionary](https://github.com/Cas1997/Physics-dictionary/) built using python and flask.

# Install on Linux

Create a virtual environment

    python3 -m venv venv
    source venv/bin/activate
    pip install .

Run the Flask webserver

    export FLASK_APP=physics_dictionary_web
    export FLASK_ENV=development
    flask init-db # only need to run this once
    flask run

# Install on Windows (When python 3 is default)

    python -m venv venv
    venv\Scripts\activate
    pip install .
    
Run the Flask webserver

    set FLASK_APP=physics_dictionary_web
    set FLASK_ENV=development
    flask init-db # only need to do this once
    flask run

# Both

To deactivate, do
    
    deactivate

Comment: You will probably have to do 
    
    pip install requests

# The Dictionary

Currently, the dictionary is pulled directly from the repository mentioned above during `flask init-db`.
