# -*- coding: utf-8 -*-


import os


class Configuration(object):
    NAME = 'raspberry-home-auto'
    DEBUG = True
    COMPRESS_LEVEL = 9
    ASSETS_DEBUG = True
    MONGODB_URI = os.environ.get("MONGODB_URI") if DEBUG == False else "mongodb://localhost:27017/raspberry-home-auto"
    REDIS_URI = os.environ.get("REDIS_URL") if DEBUG == False else "redis://localhost:6379/0"
