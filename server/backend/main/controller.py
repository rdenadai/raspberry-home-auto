# -*- coding: utf-8 -*-


from flask import current_app, Blueprint, render_template, abort


main = Blueprint('main', __name__, template_folder='templates')
