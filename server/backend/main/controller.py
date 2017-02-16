# -*- coding: utf-8 -*-


import ujson
from flask import current_app, Blueprint, render_template, abort
from flask import request
from ..configuration import Configuration
from ..database import Database


main = Blueprint('main', __name__, template_folder='templates')
