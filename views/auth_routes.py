from . import auth_routes
from controllers import auth_controller


@auth_routes.route("/login", methods=['GET'])
def login():
    return auth_controller.AuthenticationController.login()

