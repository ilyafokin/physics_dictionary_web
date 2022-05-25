import json
import requests
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    
    acronyms_dict = {}
    # with open('physics_dictionary_web/static/PhysicsDictionary.json', 'r') as f:
    #     acronyms_dict = json.load(f)
    acronyms_dict = requests.get('https://raw.githubusercontent.com/Cas1997/Physics-dictionary/main/PhysicsDictionary.json').json()
    
    for key in acronyms_dict:
        description, tags, webpage = acronyms_dict.get(key)[0]
        db.execute(
            "INSERT INTO acronyms (acronym, descr, webpage, tags) VALUES (?, ?, ?, ?)",
            (key, description, webpage, tags),
        )
        db.commit()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
