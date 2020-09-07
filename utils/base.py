import os
import pathlib

__all__ = ("BaseFile", "BaseBatchFiles")

class BaseFile:

    def __init__(self, filename, to_filename, **kwargs):
        self.filename = filename
        self.to_filename = to_filename
        self.replace = kwargs.get("replace", False)


    def get_format(self, filename):
        name, extension = os.path.splitext(filename)
        print("name", name)
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
        self.newdir = kwargs.get("outputdir", self.dirpath+'_'+self.to_format)

    
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
        


