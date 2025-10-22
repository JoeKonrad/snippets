import pytesseract
from pdf2image import convert_from_path
import os

popplerPath = r'path/to/poppler/bin' #EXAMPLE C:\Whatever\location\thats\relevant\poppler-25.07.0\Library\bin
dirPath = r'your/dir/here' #windows is r'a\b' or 'a\\b'
contents = os.listdir(dirPath)

files = [f for f in contents if os.path.isfile(os.path.join(dirPath, f))]

for x in files:
    images = convert_from_path(dirPath+'\\'+x,poppler_path = popplerPath)
    print(images)
