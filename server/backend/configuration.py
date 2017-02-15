# -*- coding: utf-8 -*-


import os


class Configuration(object):
    HASH_KEY = '5ac9105f-7db2-4366-988a-90ea2f191acb'
    NAME = 'raspberry-home-auto'
    STATIC_FOLDER = 'frontend/static'
    TEMPLATE_FOLDER = 'frontend/templates'
    DEBUG = True
    COMPRESS_LEVEL = 9
    ASSETS_DEBUG = True
    MONGODB_URI = os.environ.get("MONGODB_URI") if DEBUG == False else "mongodb://localhost:27017/raspberry-home-auto"
    REDIS_URI = os.environ.get("REDIS_URL") if DEBUG == False else "redis://localhost:6379/0"
