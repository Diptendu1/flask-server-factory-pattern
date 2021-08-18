from . import routes
from controllers import main_controller
from controllers import controller_object_oriented


@routes.route("/", methods=['GET'])
def index():
    return "Base API"


@routes.route("/first", methods=['GET'])
def first():
    return main_controller.first()


@routes.route("/geturlres", methods=['GET'])
async def get_url_res():
    return main_controller.get_json("https://api.publicapis.org/entries")


@routes.route("/addrole", methods=["POST"])
def add_role():
    return main_controller.add_role()


@routes.route("/adduser", methods=["POST"])
def add_user():
    return main_controller.add_user()


@routes.route("/add_user_role", methods=["POST"])
def add_user_role():
    return main_controller.add_user_role()


@routes.route("/getusers", methods=["GET"])
def get_users():
    return main_controller.get_all_users()


@routes.route("/getuser", methods=["GET"])
def get_user():
    return main_controller.get_user_details_by_id()


@routes.route("/change_username", methods=["PUT"])
def change_username():
    return controller_object_oriented.ControllerObject.change_username()

@routes.route("/delete_user", methods=["DELETE"])
def delete_user():
    return controller_object_oriented.ControllerObject.delete_user()


