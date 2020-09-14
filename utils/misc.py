import PyPDF2
import os

def rotate_pdf(path, degrees=90):

    outpath = str(degrees) + '_' + path
    with open(path, 'rb') as in_pdf:

        reader = PyPDF2.PdfFileReader(in_pdf)
        writer = PyPDF2.PdfFileWriter()

        for pnum in range(reader.numPages):
            page = reader.getPage(pnum)
            page.rotateClockwise(degrees)
            writer.addPage(page)


        with open(outpath, 'wb') as out_pdf:
            writer.write(out_pdf)

    print(f"'{path}' rotated {degrees} degrees")

    return True



def get_format(filename):
    name, extension = os.path.splitext(filename)
    return (name, extension[1:].lower())

