from flask import Flask
from flask_cors import CORS

from views.app_routes import routes


class Config:
    pass


def create_app():
    app = Flask(__name__)
    #app.config.from_object(Config)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization,x-api-key"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,OPTION,PUT,POST,DELETE"
        )
        return response

    app.register_blueprint(routes)
    return app
