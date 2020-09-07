from .base import BaseFile, BaseBatchFiles
from PIL import Image
import os

class ImageFile(BaseFile):

    PIL_KEYS = {
        "png":"png",
        "jpg":"jpeg",
        "jpeg":"jpeg",
        "webp":"webp",
        "pdf":"pdf",
    }

    def open(self, filename):
        return Image.open(filename)

    def convert(self, **kwargs):
        
        image = self.open(self.filename)

        image.convert("RGB")
        image.save(self.to_filename, self.PIL_KEYS[self.get_format(self.to_filename)[1]])
        super().convert()


class ImageBatchFiles(BaseBatchFiles):

    PIL_KEYS = {
        "png":"png",
        "jpg":"jpeg",
        "jpeg":"jpeg",
        "webp":"webp",
        "pdf":"pdf",
    }

    accepted_formats = ["png", "jpg", "jpeg", "webp"]

    def open(self, filename):
        image = ImageFile.open(self, filename)
        return image


    def convert_file(self, **kwargs):
        name = kwargs.get('name')
        extension = kwargs.get('extension')
        to_format = kwargs.get('to_format')
        save_path = os.path.join(self.newdir, os.path.split(name)[1]+'.'+to_format)

        image = self.open(name+'.'+extension)
        image.convert("RGB")
        image.save(save_path, self.PIL_KEYS[to_format])

        super().convert_file(original=name+'.'+extension, result=save_path)




