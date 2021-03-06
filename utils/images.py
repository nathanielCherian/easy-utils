from .base import BaseFile, BaseBatchFiles
from PIL import Image, ImageGrab
import os


def rotate(image, degrees):

    degrees = degrees % 360
    assert degrees % 90 == 0, "Invalid degrees for rotation! Choose from 90, 180, 270."
    if degrees == 0: # dont be this guy
        return image 

    attrs = {
        90:'ROTATE_90',
        180:'ROTATE_180',
        270:'ROTATE_270',
    }

    image = image.transpose(getattr(Image, attrs[degrees]))
    return image

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

        # Image kwargs
        if kwargs.get('r'):
            image = rotate(image, kwargs['r'])

        image.save(self.to_filename, self.PIL_KEYS[self.get_format(self.to_filename)[1]])
        super().convert()



class ImageBatchFiles(BaseBatchFiles):

    PIL_KEYS = {
        "png":"png",
        "jpg":"jpeg",
        "jpeg":"jpeg",
        "webp":"webp",
        "pdf":"pdf", # spdf is seperated pdf for batch files
    }

    accepted_formats = ["png", "jpg", "jpeg", "webp"]

    def open(self, filename):
        image = ImageFile.open(self, filename)
        return image

    def convert(self, **kwargs):

        if self.to_format == 'pdf':
            self.newdir += ".pdf"
            self.images_to_pdf(**kwargs)
        else:
            super().convert(**kwargs)


    def convert_file(self, **kwargs):
        name = kwargs.get('name')
        extension = kwargs.get('extension')
        to_format = kwargs.get('to_format')
        save_path = os.path.join(self.newdir, os.path.split(name)[1]+'.'+to_format)

        image = self.open(name+'.'+extension)
        image.convert("RGB")

        # Image kwargs
        if kwargs.get('r'):
            image = rotate(image, kwargs['r'])

        image.save(save_path, self.PIL_KEYS[to_format])

        super().convert_file(original=name+'.'+extension, result=save_path)



    # modified convert, unique to image class
    def images_to_pdf(self, **kwargs):

        images = []
        for root, _, files in os.walk(self.dirpath):

            for file_ in files:
                file_ = os.path.join(root, file_)
                _, extension = self.get_format(file_)
                if extension in self.accepted_formats:
                    images.append(self.open(file_))
                else:
                    print(f"skipped '{file_}'")


        # Image kwargs ====================================
        if kwargs.get('r'):
            for i in range(len(images)):
                images[i] = rotate(images[i], kwargs['r'])
        # ==================================================



        images[0].save(self.newdir, 'PDF', resolution=kwargs.get('resolution', 100.0), save_all=True, append_images=images[1:])

        super().convert_file(original=self.dirpath, result=self.newdir)
        
                


#Miscellanous functions
def image_from_clipboard(filename='image.png'):
    image = ImageGrab.grabclipboard()
    assert image, Exception("clipboard does not contain image")
    image.save(filename, 'PNG')
    print("Image saved from clipboard!")
    return True




