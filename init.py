import subprocess
import os
import re

def clone_server_hosting():
    if os.path.isdir('eldewrito-server-hosting'):
        print("Pulling changes from eldewrito-server-hosting repository")
        subprocess.run(["git", "pull"], cwd="eldewrito-server-hosting")
    else:
        print("Cloning eldewrito-server-hosting repository")
        repo_url = "https://gitlab.com/Insan1ty0ne/eldewrito-server-hosting.git"
        subprocess.run(["git", "clone", repo_url])

def copy_maps_and_gametypes():
    print("Copying maps and gametypes")
    game_variants_path = "eldewrito-server-hosting/0. Stock maps and gametypes/data/game_variants/"
    subprocess.run(["cp", "-r", game_variants_path, "eldewrito/data/game_variants"])
    map_variants_path = "eldewrito-server-hosting/0. Stock maps and gametypes/data/map_variants/"
    subprocess.run(["cp", "-r", map_variants_path, "eldewrito/data/map_variants"])
    mods_json_path = "eldewrito-server-hosting/5. Mixed Mods Variety/data/server/mods.json"
    subprocess.run(["cp", mods_json_path, "eldewrito/data/server/mods.json"])

def list_server_option():
    list = os.listdir('eldewrito-server-hosting')
    list = [x for x in list if x != '0. Stock maps and gametypes']
    # keep only directories that begin with a number
    list = [x for x in list if x[0].isdigit()]
    return list

def list_to_name(list):
    name_list = []
    for option in list:
        name_list.append(option.split(' ')[1].lower() + '_' + option.split(' ')[2].lower())
    return name_list

def copy_voting(server_option):
    name_option = list_to_name(server_option)
    if not os.path.isdir('eldewrito/data/voting'):
        os.mkdir('eldewrito/data/voting')
    for i, option in enumerate(server_option):
        voting_json_path = f"eldewrito-server-hosting/{option}/data/server/voting.json"
        subprocess.run(["cp", voting_json_path, f"eldewrito/data/voting/voting_{name_option[i]}.json"])

def update_setting(setting, value, config_file_link):
    if value:
        with open(config_file_link, 'r+') as file:
            content = file.read()
            content_new = re.sub(f'^{setting} \"[^\"]*\"', f'{setting} "{value}"', content, flags=re.MULTILINE)
            file.seek(0)
            file.write(content_new)
            file.truncate()
    
if __name__ == "__main__":
    # clone_server_hosting()
    # copy_maps_and_gametypes()
    list = list_server_option()
    # copy_voting(list)
    update_setting('Server.Name', 'khjlfgsakjh Server', 'eldewrito/data/server_0.cfg')