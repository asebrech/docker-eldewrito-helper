import subprocess
import os
import re

from src.utils.utils import get_list_server_hosting, list_to_name, name_to_suffix, remove_items

YELLOW = "\033[93m"
END = "\033[0m"

def clone_server_hosting(commit_hash):
    if os.path.isdir('eldewrito-server-hosting'):
        print(f"{YELLOW}Pulling changes from eldewrito-server-hosting repository{END}")
        subprocess.run(["git", "pull"], cwd="eldewrito-server-hosting")
    else:
        print(f"{YELLOW}Cloning eldewrito-server-hosting repository{END}")
        repo_url = "https://gitlab.com/Insan1ty0ne/eldewrito-server-hosting.git"
        subprocess.run(["git", "clone", repo_url])
    # print(f"Checking out to commit {commit_hash}")
    # subprocess.run(["git", "checkout", commit_hash], cwd="eldewrito-server-hosting", stdout=subprocess.DEVNULL)

def clone_docker_eldewrito(commit_hash):
    if os.path.isdir('docker-eldewrito'):
        print(f"{YELLOW}Pulling changes from eldewrito repository{END}")
        subprocess.run(["git", "pull"], cwd="eldewrito")
    else:
        print(f"{YELLOW}Cloning eldewrito repository{END}")
        repo_url = "https://github.com/thebeerkeg/docker-eldewrito.git"
        subprocess.run(["git", "clone", repo_url])
    # print(f"Checking out to commit {commit_hash}")
    # subprocess.run(["git", "checkout", commit_hash], cwd="docker-eldewrito", stdout=subprocess.DEVNULL)

def copy_maps_and_gametypes():
    print(f"{YELLOW}Copying maps and gametypes{END}")
    game_variants_path = "eldewrito-server-hosting/0. Stock maps and gametypes/data/game_variants/"
    subprocess.run(["cp", "-r", game_variants_path, "eldewrito/data/game_variants"])
    map_variants_path = "eldewrito-server-hosting/0. Stock maps and gametypes/data/map_variants/"
    subprocess.run(["cp", "-r", map_variants_path, "eldewrito/data/map_variants"])
    mods_json_path = "eldewrito-server-hosting/5. Mixed Mods Variety/data/server/mods.json"
    subprocess.run(["cp", mods_json_path, "eldewrito/data/server/mods.json"])


def copy_voting(server_option):
    print(f"{YELLOW}Copying voting files{END}")
    name_option = list_to_name(server_option)
    if not os.path.isdir('eldewrito/data/voting'):
        os.mkdir('eldewrito/data/voting')
    for i, option in enumerate(server_option):
        voting_json_path = f"eldewrito-server-hosting/{option}/data/server/voting.json"
        subprocess.run(["cp", voting_json_path, f"eldewrito/data/voting/voting_{name_to_suffix(name_option[i])}.json"])

def init():
    commit_hash = "4ab78fae4ba825197a245ec8a1d5096a077a6553"
    clone_server_hosting(commit_hash)
    commit_hash = "cf9b3ba5502a1d0bf454421486c82e3314919dad"
    clone_docker_eldewrito(commit_hash)
    copy_maps_and_gametypes()
    list_server_hosting = get_list_server_hosting()
    items_to_remove = ['0. Stock maps and gametypes', '6. Minimal example']
    list_server_hosting = remove_items(list_server_hosting, items_to_remove)
    copy_voting(list_server_hosting)
    