"""Converts png, bmp and gif to jpg, removes descriptions and resizes the image to a maximum of 1920x1080."""

from PIL import Image
from glob import glob
import PIL
import sys
import os


path = '/home/howard/Homework/Algorithm/Final_Project/handwrite_detect_new/train_image/0/'
path_originals = '/home/howard/Homework/Algorithm/Final_Project/handwrite_detect/train_image/0/'

if not os.path.exists(path):
    os.makedirs(path)


def processImage():
    listing = os.listdir(path_originals)
    for infile in listing:
        img = Image.open(path_originals+infile)
        name = infile.split('.')
        first_name = path+'/'+name[0] + '.jpg'

        image = img.convert('RGB')
        img.close()

processImage()