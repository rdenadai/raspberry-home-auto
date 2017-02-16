# -*- coding: utf-8 -*-


import ujson
import time
from bson.json_util import dumps
from flask import jsonify
from flask import current_app, Blueprint, render_template, abort
from flask import request
from ..configuration import Configuration
from ..database import Database
from ..message import Message


network = Blueprint('network', __name__, template_folder='templates')


@network.route('/save/', methods=['POST'])
def save():
    response = {
        'error': True,
        'message': '',
        'data': None
    }

    hash_key = request.form.get('hashkey')
    network = ujson.loads(request.form.get('network'))

    if hash_key == Configuration.HASH_KEY:
        db = Database.get_mongodb_database()
        if db:
            db.network.insert_one(network)
            response['error'] = False
            response['data'] = network
        else:
            response['message'] = Message.INVALID_DATABASE
    else:
        response['message'] = Message.NO_HASH_KEY
    return jsonify(response)


@network.route('/get/')
@network.route('/get/<hash_key>')
def get(hash_key=None):
    response = {
        'error': True,
        'message': '',
        'data': None
    }

    if hash_key == Configuration.HASH_KEY:
        db = Database.get_mongodb_database()
        if db:
            response['error'] = False
            response['data'] = ujson.loads(dumps(db.network.find()[0]))
        else:
            response['message'] = Message.INVALID_DATABASE
    else:
        response['message'] = Message.NO_HASH_KEY
    return jsonify(response)
