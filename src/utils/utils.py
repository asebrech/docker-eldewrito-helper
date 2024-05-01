import os

def get_list_server_hosting():
    list = os.listdir('eldewrito-server-hosting')
    list = [x for x in list if x[0].isdigit()]
    return list

def list_to_name(list):
    name_list = []
    for option in list:
        name_list.append(option.split(' ')[1] + ' ' + option.split(' ')[2])
    return name_list

def name_to_suffix(name):
    words = name.split(' ')
    suffix = '_'.join(word.lower() for word in words)
    return suffix