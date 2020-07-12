import random,os
import asyncio
import uvloop
from pymongo import MongoClient
from sanic import Sanic,response, Blueprint
from sanic_mongodb_ext import MongoDbExtension
from umongo import Instance, Document, MotorAsyncIOInstance
from config import MONGODB_SETTINGS
import config


pymongo_db = None
MONGO_DB_HOST = os.getenv("MONGODB_URI") or "localhost"
MONGO_DB_NAME = os.getenv("DB_NAME") or "imdbmovie"

def get_pymongo_client():
    global pymongo_db
    if pymongo_db is None:
        pymongo_client = MongoClient(MONGODB_SETTINGS["HOST"])
        pymongo_db = pymongo_client[MONGODB_SETTINGS["DB"]]
    return pymongo_db

instance = Instance(get_pymongo_client())

def create_app():
    """Initialize the core application."""
    app = Sanic(__name__)

    #loading configurations
    app.config.from_object(config)
    app.config["MONGODB_SETTINGS"] = {
        "db": MONGO_DB_NAME,
        "host": MONGO_DB_HOST,
    }

    # Register Blueprints
    from .api.v1.movies.handler import movie_views
    from .api.v1.users.handler import user_views
    app.register_blueprint(movie_views)
    app.register_blueprint(user_views)
    return app

