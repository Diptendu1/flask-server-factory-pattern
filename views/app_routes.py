from . import routes
from controllers import main_controller


@routes.route("/")
def index():
    return "BAse API"


@routes.route("/api/v1/first")
def first():
    return main_controller.first()
