from ..service.RoleService import RoleService


class HTMLUtility:

    @staticmethod
    def get_list_from_dict(name, selected_val='', data_dict={}):
        sb = [
            f"<select style=\"width: 170px; text-align-last: center;\" class='form-control' name='{name}'>"
        ]
        sb.append("\n<option selected value=''>-------------Select-------------</option>")

        for key, val in data_dict.items():
            if key == selected_val:
                sb.append(f"\n<option selected value='{key}'>{val}</option>")
            else:
                sb.append(f"\n<option value='{key}'>{val}</option>")
        sb.append("\n</select>")
        return "".join(sb)

    @staticmethod
    def get_list_from_objects(name, selected_val=0, data_list={}):
        sb = [
            f"<select style=\"width: 170px; text-align-last: center;\" class='form-control' name='{name}'>"
        ]
        sb.append("\n<option selected value=''>-------------Select-------------</option>")

        for obj in data_list:
            key = obj.get_key()
            val = obj.get_value()

            if key == str(selected_val):
                sb.append(f"\n<option selected value='{key}'>{val}</option>")
            else:
                sb.append(f"\n<option value='{key}'>{val}</option>")

        sb.append("\n</select>")
        return "".join(sb)
