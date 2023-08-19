import argparse
from PIL import Image
from math import ceil

parser = argparse.ArgumentParser()
parser.add_argument("filenames", nargs='+')
args = parser.parse_args()

# print(args.filenames)

def crop(imgfile, padratio=0.0333):
    img = Image.open(imgfile)
    x0, y0, x1, y1 = img.getbbox()
    padding = ceil(max(x1-x0, y1-y0) * padratio)
    img = img.crop((x0-padding, y0-padding, x1+padding, y1+padding))
    img.save(imgfile)

def process():
    for file in args.filenames:
        crop(file)

# code.interact(local=locals())

process()

print("Process Completed.")