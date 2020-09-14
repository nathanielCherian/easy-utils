from . import __title__, __version__, ACCEPTED_FORMATS
from .images import ImageFile, ImageBatchFiles, image_from_clipboard
from .base import BaseBatchFiles
from .misc import rotate_pdf, get_format

import argparse
import textwrap



command_help = """\
Commands:
  /command [arg2]  : info
  /cb [SAVE PATH]  : copy image from clipboard
  /rpdf [PDF PATH] : rotates pdf

"""

def parse_args():
    parser = argparse.ArgumentParser(prog='utils',
    formatter_class=argparse.RawDescriptionHelpFormatter, 
    epilog= textwrap.dedent(command_help))

    parser.add_argument("--version", "-v", action="version", version=f"{__title__} {__version__}")

    help = "base file or command"
    parser.add_argument("arg1", help=help)

    help = "Desired file name+extension"
    parser.add_argument("arg2", help=help)

    help = "rotate image/pdf with action R°"
    parser.add_argument('-r', action="store", help=help)


    args = parser.parse_args()

    return args



commands = {
    "/cb":lambda filename: image_from_clipboard(filename=filename),
    '/rpdf':lambda path: rotate_pdf(path)
}

def args_to_class(args):


    if '.' in args.arg1:
        _, format_ = get_format(args.arg1)
        ConvertFile = ACCEPTED_FORMATS.get(format_, None)["SINGLE"]
        return ConvertFile

    else:
        ConvertBatchFile = ACCEPTED_FORMATS.get(args.arg2.lower(), None)["BATCH"]
        return ConvertBatchFile

    return


def main():
    
    args = parse_args()

    print(args)
    #try:


    if args.arg1[0] == '/' and commands.get(args.arg1, lambda *args: False)(args.arg2):
        return True


    ConvertFile = args_to_class(args)
    if ConvertFile:

            my_file = ConvertFile(args.arg1, args.arg2)
            my_file.convert(**args.__dict__)


    else:
        print("arguments not found.")


    #except Exception as e:
    #    print(e)

    """
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

    """

if __name__ == "__main__":
    main()