import re
import csv

def identify_file_type(filename):
    # with open a file and read it in binary mode
    with open(filename, 'rb') as file:
        binary_data = file.read()
    
    hex_data = binary_data.hex()
    
    # JPEG: ffd8ffe0
    # ZIP: 504b0304
    # PDF: 25504446
    
    import re

    # define the regular expressions for file signatures
    jpeg_regex = re.compile(r'^ffd8ffe0')
    zip_regex = re.compile(r'^504b0304')
    pdf_regex = re.compile(r'^25504446')

    # check if the file is a JPEG
    if re.match(jpeg_regex, hex_data[0:8]):
        print('This is a JPEG file.')

    # check if the file is a ZIP
    elif re.match(zip_regex, hex_data[0:8]):
        print('This is a ZIP file.')

    # check if the file is a PDF
    elif re.match(pdf_regex, hex_data[0:8]):
        print('This is a PDF file.')

    else:
        print('This is an unknown file type.')

if __name__ == "__main__":
    filename=input("Enter the filename: ")
    identify_file_type(filename)
