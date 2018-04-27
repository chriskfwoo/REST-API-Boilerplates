import os
from flask import Flask
from flask import Blueprint
from config import app_config
from flask_jwt_extended import JWTManager


def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    jwt = JWTManager(app)

    from auth.login import auth_bp
    app.register_blueprint(auth_bp)

    from api.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from model import db
    db.init_app(app)

    return app

