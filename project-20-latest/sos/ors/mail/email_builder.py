class EmailBuilder:

    @staticmethod
    def sign_up(obj):
        msg = ""
        msg += "Welcome to ORS!\n"
        msg += "Your registration was successful.\n\n"
        msg += f"Login ID: {obj.login_id}\n"
        msg += f"Password: {obj.password}\n\n"
        msg += "Log in at: https://www.raysedtech.com/\n"
        msg += "Please change your password after first login for security.\n"
        return msg

    @staticmethod
    def change_password(obj):
        msg = ""
        msg += "Password Changed Successfully\n"
        msg += f"Hi {obj.firstName} {obj.lastName}, your password has been updated.\n\n"
        msg += f"Login ID: {obj.loginId}\n"
        msg += f"New Password: {obj.password}\n"
        return msg

    @staticmethod
    def forgot_password(obj):
        msg = ""
        msg += "Password Recovery\n"
        msg += f"Hi {obj.firstName} {obj.lastName}, here are your login details:\n\n"
        msg += f"Login ID: {obj.loginId}\n"
        msg += f"Password: {obj.password}\n"
        return msg
