import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from physics_dictionary_web.db import get_db

bp = Blueprint('lookup', __name__, url_prefix='/')

@bp.route('/', methods=('GET', 'POST'))
def lookup():
    acronym = None
    description = None
    webpage = None
    if request.method == 'POST':
        acronym = request.form['acronym']
        db = get_db()
        error = None

        if not acronym:
            error = 'No search term given'
        
        if error is None:
            entry = db.execute(
            'SELECT * FROM acronyms WHERE acronym = ?', (acronym,)
            ).fetchone()
        
        if entry is None:
            error = 'No match found.'
        else:
            description = entry['descr']
            webpage = entry['webpage'] if entry['webpage'] != '' else None
    print(acronym, description, webpage)

    return render_template('content.html', acronym=acronym, description=description, webpage=webpage)