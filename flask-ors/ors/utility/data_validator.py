class DataValidator:

    @staticmethod
    def is_null(val):
        if val == '' or val is None:
            return True
        else:
            return False


    @staticmethod
    def is_not_null(val):
        if val is None or val == '':
            return False
        else:
            return True