import os
import pathlib
from .misc import get_format

__all__ = ("BaseFile", "BaseBatchFiles")

class BaseFile:

    def __init__(self, filename, to_filename, **kwargs):
        self.filename = filename
        self.replace = kwargs.get("replace", False)

        self.initialize(filename, to_filename, **kwargs)


    def initialize(self, filename, to_filename, **kwargs):
        if '.' in to_filename:
            self.to_filename = to_filename
        else:
            name, _ = self.get_format(filename)
            self.to_filename = name+'.'+to_filename



    def get_format(self, filename):
        name, extension = os.path.splitext(filename)
        return (name, extension[1:].lower())


    def open(self):
        return

    def convert(self, **kwargs):
        
        if kwargs.get("verbose", True):
            print(f"'{kwargs.get('original') or self.filename}' -->  '{kwargs.get('result') or self.to_filename}'")

        return


class BaseBatchFiles(BaseFile):

    accepted_formats = []

    def __init__(self, dirpath, to_format, **kwargs):
        self.dirpath = dirpath
        self.to_format = to_format

        self.initialize(dirpath, to_format, **kwargs)

    def initialize(self, dirpath, to_format, **kwargs):

        if '.' in to_format:
            assert get_format(to_format)[1] == 'pdf', 'Must provide a name of .pdf type!'
            name, format_ = get_format(to_format)
            self.newdir = name
            self.to_format = format_
        else:
            self.newdir = self.dirpath+'_'+self.to_format


    
    def convert(self, **kwargs):
        
        pathlib.Path(self.newdir).mkdir(parents=True, exist_ok=True)

        for root, _, files in os.walk(self.dirpath):

            for file_ in files:
                file_ = os.path.join(root, file_)
                name, extension = self.get_format(file_)
                if extension in self.accepted_formats:
                    self.convert_file(name=name, extension=extension, to_format=self.to_format)
                else:
                    print(f"skipped '{file_}'")

        


    def convert_file(self, **kwargs):
        BaseFile.convert(self, **kwargs)
        


