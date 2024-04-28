import os

def list_server_option():
    list = os.listdir('eldewrito-server-hosting')
    list = [x for x in list if x != '0. Stock maps and gametypes']
    # keep only directories that begin with a number
    list = [x for x in list if x[0].isdigit()]
    return list

def name_to_suffix(name):
    words = name.split(' ')
    suffix = '_'.join(word.lower() for word in words)
    return suffix