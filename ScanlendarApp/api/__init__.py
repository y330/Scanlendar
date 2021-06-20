from flask import Flask
from flask_marshmallow import Marshmallow
from flask_mongoengine import MongoEngine
from .routes import scan_api

# DATABASE 
db = MongoEngine()

# SERIALIZER
ma = Marshmallow()

def initialize_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = ''
    app.config["MONGODB_SETTINGS"] = {
        'db': '', 
        'host': '', 
        'port': 0, 
    }

    # Initialize Secret Key and Setup DB Config
    # Register Blueprints

    ma.init_app(app)
    db.init_app(app)

    app.register_blueprint(scan_api, url_prefix="/api")

    return app