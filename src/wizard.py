import questionary
import sys
from questionary import ValidationError, Validator
from src.generate_compose import generate_docker_compose
from src.utils.utils import get_list_server_hosting, list_to_name, name_to_suffix, remove_items

YELLOW = "\033[93m"
END = "\033[0m"

class NotEmptyValidator(Validator):
    def validate(self, document):
        if not document.text:
            raise ValidationError(
                message="Please enter a value",
                cursor_position=len(document.text))
        
class NumberValidator(Validator):
    def validate(self, document):
        if not document.text.isdigit():
            raise ValidationError(
                message="Please enter a number",
                cursor_position=len(document.text))
        if int(document.text) < 1 or int(document.text) > 20:
            raise ValidationError(
                message="Please enter a number between 1 and 20",
                cursor_position=len(document.text))

def wizard():
    list_server_hosting = get_list_server_hosting()
    items_to_remove = ['0. Stock maps and gametypes', '6. Minimal example']
    list_server_hosting = remove_items(list_server_hosting, items_to_remove)
    server_names = list_to_name(list_server_hosting)
    config_data = {}
    server = []

    config_data["host_name"] = questionary.text("🍕 Name of the server host that will appear in the server browser ?", validate=NotEmptyValidator).ask()
    config_data["rcon_password"] = questionary.text("🍺 RCON password ?", validate=NotEmptyValidator).ask()

    if not config_data["host_name"] or not config_data["rcon_password"]:
        print("One or more required values are missing. Exiting program.")
        sys.exit(0)

    while True:
        server_info = {}
        server_info["selected_server"] = questionary.select("🌮 Please select a mod to configure:", choices=server_names,).ask()
        server_info["server_name"] = questionary.text("🧀 Name of your server ?", validate=NotEmptyValidator).ask()
        server_info["server_message"] = questionary.text("🥪 Server message that will display on loading screens ?", validate=NotEmptyValidator).ask()
        server_info["server_intance"] = questionary.text("🍔 Number of instance of this server ?", validate=NumberValidator).ask()

        if None in server_info.values():
            print("One or more required values are missing. Exiting program.")
            sys.exit(0)

        server_names.remove(server_info["selected_server"])
        server.append(server_info)

        reselect = questionary.confirm("Do you want to select another mod?").ask()
        if not reselect or not server_names:
            break

    config_data["server"] = server   
    docker_compose_content = generate_docker_compose(config_data)
    with open("docker-compose.yml", "w") as f:
        f.write(docker_compose_content)
    print(f"🍰 {YELLOW}docker-compose.yml file generated successfully{END}")

