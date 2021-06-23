from flask import Flask
from flask_marshmallow import Marshmallow
import os
from flask_sqlalchemy import SQLAlchemy
from .routes import scan_api

basedir = os.path.abspath(os.path.dirname(__file__))

# DATABASE
db = SQLAlchemy()

# SERIALIZER
ma = Marshmallow()

def initialize_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = ''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize Secret Key and Setup DB Config
    # Register Blueprints

    ma.init_app(app)
    db.init_app(app)

    app.register_blueprint(scan_api, url_prefix = "/api")

    return app