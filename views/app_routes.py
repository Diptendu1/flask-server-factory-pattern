from . import routes
from controllers import main_controller


@routes.route("/", methods=['GET'])
def index():
    return "Base API"


@routes.route("/api/v1/first", methods=['GET'])
def first():
    return main_controller.first()


@routes.route("/api/v1/geturlres", methods=['GET'])
async def get_url_res():
    return main_controller.get_json("https://api.publicapis.org/entries")


@routes.route("/api/v1/addrole", methods=["POST"])
def add_role():
    return main_controller.add_role()


@routes.route("/api/v1/adduser", methods=["POST"])
def add_user():
    return main_controller.add_user()


@routes.route("/api/v1/add_user_role", methods=["POST"])
def add_user_role():
    return main_controller.add_user_role()


@routes.route("/api/v1/getusers", methods=["GET"])
def get_users():
    return main_controller.get_all_users()