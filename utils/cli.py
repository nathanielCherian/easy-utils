from . import __title__, __version__
from .images import ImageFile, ImageBatchFiles, image_from_clipboard
from .base import BaseBatchFiles
from .misc import rotate_pdf

import argparse

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--version", "-v", action="version", version=f"{__title__} {__version__}")

    help = "Base file that you have"
    parser.add_argument("arg1", help=help)

    help = "Desired file name+extension"
    parser.add_argument("arg2", help=help)

    args = parser.parse_args()

    return args


commands = {
    "/cb":lambda filename: image_from_clipboard(filename=filename),
    '/rpdf':lambda path: rotate_pdf(path)
}


def main():
    
    args = parse_args()

    print(args.arg1, args.arg2)


    commands.get(args.arg1, lambda *args: None)(args.arg2)
    


    #try:

    #BaseBatchFiles(args.arg1, args.arg2).convert()

    if '.' in args.arg1:

        my_file = ImageFile(args.arg1, args.arg2)
        my_file.convert()

    else:
        ImageBatchFiles(args.arg1, args.arg2).convert()

    #except Exception as e:
    #    print("ERROR")
    #    print(e)




if __name__ == "__main__":
    main()