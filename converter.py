import os

from PIL import Image

for filename in os.listdir('./images4'):
    im = Image.open(r'./images4/' + filename)
    im.save(r'./images4/' + filename[:-3] + 'png')