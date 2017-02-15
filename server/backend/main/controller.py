# -*- coding: utf-8 -*-


import ujson
from flask import current_app, Blueprint, render_template, abort
from flask import request
from backend.configuration import Configuration
from backend.database import Database


main = Blueprint('main', __name__, template_folder='templates')


@main.route('/rest/network/')
def network():
    hash_key = request.form.get('hashkey')
    network = ujson.loads(request.form.get('network'))

    if hash_key == Configuration.HASH_KEY:
        db = Database.get_mongodb_database()
        if db:
            db.network.insert_one(network)
