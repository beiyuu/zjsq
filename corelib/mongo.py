from flask.ext.pymongo import PyMongo
from homeland import app

mongo = PyMongo(app)
