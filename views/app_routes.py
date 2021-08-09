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
    return main_controller.insert_data_ex()