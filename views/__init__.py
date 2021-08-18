from flask import Blueprint
routes = Blueprint("routes", __name__, url_prefix='/api/v1')
auth_routes = Blueprint("auth_routes", __name__, url_prefix='/api/v1/auth')

from . import app_routes
from . import auth_routes
