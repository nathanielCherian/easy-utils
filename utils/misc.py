import PyPDF2

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

# miscellaneous functions


