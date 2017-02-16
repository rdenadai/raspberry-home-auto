# -*- coding: utf-8 -*-


from flask import Flask
from flask import request, send_from_directory
from flask import render_template
from flask_caching import Cache
from flask_compress import Compress

from backend.configuration import Configuration

from backend.main.controller import main
from backend.network.controller import network

from werkzeug.exceptions import abort


# -----------------------------------------------------
# Flask-Compress
# -----------------------------------------------------
compress = Compress()
# -----------------------------------------------------
# Flask-Cache
# -----------------------------------------------------
cache = Cache(config={'CACHE_TYPE': 'memcached'})
# -----------------------------------------------------
# Flask Application
# -----------------------------------------------------
app = Flask(
    Configuration.NAME,
    static_folder=Configuration.STATIC_FOLDER,
    template_folder=Configuration.TEMPLATE_FOLDER
)
# -----------------------------------------------------
# Compressing to gzip integration!
# -----------------------------------------------------
compress.init_app(app)
# -----------------------------------------------------
# Caching the views integration!
# -----------------------------------------------------
cache.init_app(app)

# -----------------------------------------------------
# CONFIGURATION
# ------------------------------------------
app.config.from_object('backend.configuration.Configuration')


# -----------------------------------------------------
# DEFAULT ROUTE, ALWAYS PRINT HOME SCREEN... THIS IS A REACT APP
# -----------------------------------------------------
@app.route('/')
@cache.cached(timeout=1)
def index():
    return render_template('index.html')


# -----------------------------------------------------
# SUB PATHS INSIDE REACT APP
# -----------------------------------------------------
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if 'app' in path:
        return render_template('index.html')
    return abort(404)


# -----------------------------------------------------
# START BLUEPRINT APPS API!
# -----------------------------------------------------
app.register_blueprint(main)
app.register_blueprint(network, url_prefix='/network')
# -----------------------------------------------------
# END: BLUEPRINT APPS API!
# -----------------------------------------------------


# -----------------------------------------------------
# STATIC ROUTES TO SERVER SOME FILES!
# -----------------------------------------------------
@app.route('/robots.txt')
@app.route('/humans.txt')
@app.route('/sitemap.xml')
@app.route('/manifest.json')
@app.route('/sw.js')
@cache.cached(timeout=1)
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


# -----------------------------------------------------
# MAIN APP START!
# -----------------------------------------------------
if __name__ == "__main__":
    app.run()
