import os

class Config:

    config_data = {}
    server = []

    def __init__(self):
        self.list_server_path = self.get_list_server_hosting()
        self.list_server_option = [x for x in self.list_server_path if x != '0. Stock maps and gametypes']
        self.list_server_suffix = self.list_to_name()
        self.list_server_name = self.list_to_name()

    def get_list_server_hosting(self):
        list = os.listdir('eldewrito-server-hosting')
        list = [x for x in list if x[0].isdigit()]
        return list
    
    def list_to_name(self):
        list = self.list_server_option
        name_list = []
        for option in list:
            name_list.append(option.split(' ')[1] + ' ' + option.split(' ')[2])
        return name_list
    
    def list_to_suffix(self):
        list = self.list_server_option
        name_list = []
        for option in list:
            name_list.append(option.split(' ')[1].lower() + '_' + option.split(' ')[2].lower())
        return name_list