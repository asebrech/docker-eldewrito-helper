import argparse
import pyfiglet

from src.wizard import wizard

def main(args):
    halo = pyfiglet.figlet_format("Halo", font="smisome1")
    print(halo)
    if args.config:
        wizard()
    if args.init:
        print('You entered init')
    if args.update:
        print('You entered update')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some arguments.')
    parser.add_argument('--config', action='store_true', help='The config to process')
    parser.add_argument('--init', action='store_true', help='The init to process')
    parser.add_argument('--update', action='store_true', help='The update to process')

    args = parser.parse_args()

    if sum([args.config, args.init, args.update]) > 1:
        parser.error("You can only provide one argument at a time.")
    elif not args.config and not args.init and not args.update:
        parser.error("You must provide one argument.")
    else:
        main(args)