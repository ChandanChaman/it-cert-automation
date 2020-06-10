#!/usr/bin/env python3

#Convert all tiff images to jpeg & resize to desired size.

from PIL import Image
import os

dir ='supplier-data/images/'
for f in os.listdir(dir):
    if f.endswith('.tiff'):
        file = dir+f
        im= Image.open(file)
        im.convert('RGB').resize((600,400)).save(dir+f.strip('tiff')+'jpeg')
