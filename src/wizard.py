import questionary
from questionary import ValidationError, Validator
import sys

from src.config import Config
from src.utils.utils import name_to_suffix

class NotEmptyValidator(Validator):
    def validate(self, document):
        if not document.text:
            raise ValidationError(
                message="Please enter a value",
                cursor_position=len(document.text))  # Move cursor to end
        
class NumberValidator(Validator):
    def validate(self, document):
        if not document.text.isdigit():
            raise ValidationError(
                message="Please enter a number",
                cursor_position=len(document.text))  # Move cursor to end

def wizard():
    # new config classe
    config = Config()
    # get the server names from the config
    server_names = config.list_server_name

    config.config_data["host_name"] = questionary.text("🍕 Name of the server host that will appear in the server browser ?", validate=NotEmptyValidator).ask()
    config.config_data["rcon_password"] = questionary.text("🍺 RCON password ?", validate=NotEmptyValidator).ask()
    while True:
        server_info = {}
        server_info["selected_server"] = questionary.select("🌮 Please select a mod to configure:", choices=server_names,).ask()
        server_info["selected_server_suffix"] = name_to_suffix(server_info["selected_server"])
        server_names.remove(server_info["selected_server"])
        server_info["server_name"] = questionary.text("🧀 Name of your server ?", validate=NotEmptyValidator).ask()
        server_info["server_message"] = questionary.text("🥪 Server message that will display on loading screens ?", validate=NotEmptyValidator).ask()
        server_info["server_intance"] = questionary.text("🍰 Number of instance of this server ?", validate=NumberValidator).ask()
        config.server.append(server_info)
        reselect = questionary.confirm("Do you want to select another mod?").ask()
        if not reselect or not server_names:
            break
    config.config_data["server"] = config.server    
    print(config.config_data)
  