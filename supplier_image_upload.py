#!/usr/bin/env python3
import requests
import os

# The Python Requests module to upload all converted images

url = "http://localhost/upload/"
dir ='supplier-data/images/'

for f in os.listdir(dir):
    if f.endswith('.jpeg'):
        with open(dir+f, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
            print ('Uploaded', f)
