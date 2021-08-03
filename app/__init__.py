import logging
from flask import Flask, request
from datetime import datetime as dt
from flask_cors import CORS

from environs import Env, EnvError

from app.app_extentions import logs
from views.app_routes import routes


class Config:

    env = Env()
    env.read_env()

    # Logging Setup
    LOG_TYPE = env.str("LOG_TYPE", "stream")  # Default is a Stream handler
    LOG_LEVEL = env.str("LOG_LEVEL", "INFO")

    # File Logging Setup
    LOG_DIR = env.str("LOG_DIR", "/data/logs")
    APP_LOG_NAME = env.str("APP_LOG_NAME", "app.log")
    WWW_LOG_NAME = env.str("WWW_LOG_NAME", "www.log")
    LOG_MAX_BYTES = env.int("LOG_MAX_BYTES", 100_000_000)  # 100MB in bytes
    LOG_COPIES = env.int("LOG_COPIES", 5)


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

    app.register_blueprint(routes)
    logs.init_app(app)
    return app
