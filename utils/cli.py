from . import __title__, __version__
from .images import ImageFile, ImageBatchFiles, image_from_clipboard
from .base import BaseBatchFiles

import argparse

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--version", "-v", action="version", version=f"{__title__} {__version__}")

    help = "Base file that you have"
    parser.add_argument("base_file", help=help)

    help = "Desired file name+extension"
    parser.add_argument("desired_file", help=help)

    args = parser.parse_args()

    return args


commands = {
    "/cb":lambda filename: image_from_clipboard(filename=filename)
}


def main():
    
    args = parse_args()

    print(args.base_file, args.desired_file)


    commands.get(args.base_file, lambda *args: None)(args.desired_file)
    


    #try:

    #BaseBatchFiles(args.base_file, args.desired_file).convert()

    if '.' in args.base_file:

        my_file = ImageFile(args.base_file, args.desired_file)
        my_file.convert()

    else:
        ImageBatchFiles(args.base_file, args.desired_file).convert()

    #except Exception as e:
    #    print("ERROR")
    #    print(e)




if __name__ == "__main__":
    main()