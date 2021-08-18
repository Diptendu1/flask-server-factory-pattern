class AuthenticationController:
    @classmethod
    def login(cls):
        return_map = {}
        return_map["message"] = "Success"
        return return_map