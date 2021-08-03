from . import routes
from flask import request


@routes.route("/")
def index():
    return "First API"