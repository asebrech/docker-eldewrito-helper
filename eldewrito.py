import argparse
import os
import pyfiglet

from src.wizard import wizard
from src.init import init

YELLOW = "\033[93m"
END = "\033[0m"

def check_wizard_folder():
    if not os.path.isdir('eldewrito-server-hosting'):
        print(f"eldewrito-server-hosting folder not found, {YELLOW}python3 eldewrito.py --init{END} first")
        exit(1)
    if not os.path.isdir('docker-eldewrito'):
        print(f"docker-eldewrito folder not found, {YELLOW}python3 eldewrito.py --init{END} first")
        exit(1)
def check_eldewrito_folder():
    if not os.path.isdir('eldewrito'):
        print(f"eldewrito folder not found, {YELLOW}copy the game files to the folder{END}")
        exit(1)

def main(args):
    halo = pyfiglet.figlet_format("Halo", font="smisome1")
    print(halo)
    if args.config:
        check_wizard_folder()
        check_eldewrito_folder()
        wizard()
    if args.init:
        check_eldewrito_folder()
        init()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some arguments.')
    parser.add_argument('--config', action='store_true', help='The config to process')
    parser.add_argument('--init', action='store_true', help='The init to process')

    args = parser.parse_args()

    if sum([args.config, args.init]) > 1:
        parser.error("You can only provide one argument at a time.")
    elif not args.config and not args.init and not args.update:
        parser.error("You must provide one argument.")
    else:
        main(args)