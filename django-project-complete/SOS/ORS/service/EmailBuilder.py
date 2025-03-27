class EmailBuilder:

    @staticmethod
    def sign_up(params):
        msg = ""
        msg += "<HTML><BODY>"
        msg += "registration is Successul for ors project"
        msg += "<H1>Hi! Greetings from SunilOS!</H1>"
        msg += "<P>Congratulations for registering on ORS! You can now access your ORS account online - anywhere, anytime and enjoy the flexibility to check the Marksheet Details.</P>"
        msg += "<P>Log in today at <a href='http://ors.sunraystechnologies.com'>http://ors.sunraystechnologies.com</a> with your following credentials:</P>"
        msg += "<p><b> Login Id: " + params["login"] + "<br>" + " Password: " + params["password"] + "</b></p>"
        msg += "<P> As a security measure, we recommended that you should change your password after you first log in.</p>"
        msg += "<p>For any assistance, please feel free to call us at +91 98273 60504 or 0731-4249244 helpline numbers.</p>"
        msg += "<p>You may also write to us at hrd@sunrays.co.in.</p>"
        msg += "<p>We assure you the best service at all times and look forward to a warm and long-standing association with you.</p>"
        msg += "<P><a href='http://www.sunrays.co.in' >-SUNRAYS Technolgies</a></P>"
        msg += "</BODY></HTML>"
        return msg

    @staticmethod
    def change_password(params):
        msg = ""
        msg += "<HTML><BODY>"
        msg += "<h2>" + "Your Password has been changed successfully!! " + params.firstName + " " + params.lastName + "<h1>"
        msg += "<p><b>" + "To access account user login id: " + params.login_id + " Password : " + params.password + "</b><b>"
        msg += "</BODY></HTML>"
        return msg

    @staticmethod
    def forgot_password(params):
        print("000000000009--", params)
        print("-------------->", params.firstName)
        msg = ""
        msg += "<HTML><BODY>"
        msg += "<H1>" + "YOUR PASSWORD HAS BEEN RECOVERED" + params.firstName + " " + params.lastName + "</H1>"
        msg += "<P><B>" + "To access account user login id: " + params.loginId + "<br>" + " password: " + params.password
        msg += "</BODY></HTML>"
        return msg
