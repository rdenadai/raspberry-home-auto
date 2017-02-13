# -*- coding: utf-8 -*-


from flask import Flask
from flask import redirect, request, send_from_directory
from flask_caching import Cache
from flask_compress import Compress

from configuration import Configuration

from backend.main.controller import main


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
app = Flask(Configuration.NAME)
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
app.config.from_object('configuration.Configuration')


# -----------------------------------------------------
# START BLUEPRINT APPS API!
# -----------------------------------------------------
app.register_blueprint(main)
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
