import logging
from flask import Flask, request
from datetime import datetime as dt
from flask_cors import CORS
from settings import config
from models.core import db

from app.app_extentions import logs
from views.app_routes import routes


class Config:

    LOG_TYPE = config.get("LOG_TYPE")
    LOG_LEVEL = config.get("LOG_LEVEL")
    LOG_DIR = config.get("LOG_DIR")
    APP_LOG_NAME = config.get("APP_LOG_NAME")
    WWW_LOG_NAME = config.get("WWW_LOG_NAME")
    LOG_MAX_BYTES = config.get("LOG_MAX_BYTES")
    LOG_COPIES = config.get("LOG_COPIES")
    # Database
    SQLALCHEMY_DATABASE_URI = config.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    @app.after_request
    def after_request(response):
        """ Logging after every request. """
        logger = logging.getLogger("app.access")
        logger.info(
            "%s [%s] %s %s %s %s %s %s %s",
            request.remote_addr,
            dt.utcnow().strftime("%d/%b/%Y:%H:%M:%S.%f")[:-3],
            request.method,
            request.path,
            request.scheme,
            response.status,
            response.content_length,
            request.referrer,
            request.user_agent,
        )
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization,x-api-key"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,OPTION,PUT,POST,DELETE"
        )
        return response

    db.init_app(app)
    app.register_blueprint(routes)
    logs.init_app(app)
    return app
