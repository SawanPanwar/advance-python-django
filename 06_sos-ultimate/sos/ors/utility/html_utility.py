from ..models import DropdownItem


class HtmlUtility:

    @staticmethod
    def get_list_from_list(name: str, selected_val: str, list_data: list[str]) -> str:
        sb = [f"<select name='{name}' style='width:100%''>"]
        sb.append("<option value='0'>--Select--</option>")

        for val in list_data:
            if val == selected_val:
                sb.append(f"<option selected value='{val}'>{val}</option>")
            else:
                sb.append(f"<option value='{val}'>{val}</option>")

        sb.append("</select>")
        return "".join(sb)

    @staticmethod
    def get_list_from_beans(name: str, selected_val: int, bean_list: list[DropdownItem]) -> str:
        sb = [f"<select name='{name}' style='width:100%''>"]
        sb.append("<option value='0'>--Select--</option>")

        for obj in bean_list:
            key = obj.get_key()
            val = obj.get_value()

            if key == selected_val:
                sb.append(f"<option selected value='{key}'>{val}</option>")
            else:
                sb.append(f"<option value='{key}'>{val}</option>")

        sb.append("</select>")
        print(sb)
        return "".join(sb)
