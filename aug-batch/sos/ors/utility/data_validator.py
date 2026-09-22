class DataValidator:
    @staticmethod
    def is_null(val):
        if (val == ''):
            return True
        else:
            False
    @staticmethod
    def is_not_null(val):
        if val == None or val == "":
            return False
        else:
            return True
