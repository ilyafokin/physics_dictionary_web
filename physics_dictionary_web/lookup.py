import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from physics_dictionary_web.db2 import Dictionary

bp = Blueprint('lookup', __name__, url_prefix='/')
dict = Dictionary()

@bp.route('/', methods=('GET', 'POST'))
def lookup():
    acronym = None
    dict_tup = ()
    match = []
    descriptions = []
    close_match = False
    amount = 0
    if request.method == 'POST':
        acronym = request.form['acronym']
        error = None

        if not acronym:
            error = 'No search term given'
            

        if error is None:
            dict_tup = dict.find_result(acronym)
            match = dict_tup[0]
            close_match = dict_tup[1]
            descriptions = []
            for i in match:
                descriptions.append(dict.description(i))
            amount = len(match)
            

    return render_template('content.html', acronym=acronym, match=match, descriptions=descriptions, close_match=close_match, amount=amount)
