#!/usr/bin/python3

from PIL import Image
import sys
import time

image_width = 28
image_height = 28

image_file = open('train-images-idx3-ubyte', 'rb')
label_file = open('train-labels-idx1-ubyte', 'rb')

for i in range(10):
    image_file.seek(16 + (i*image_width*image_height), 0)
    data = image_file.read(image_width*image_height)
    img = Image.frombytes('L',(image_width,image_height),data)
    img.show()
    time.sleep(0.1)

labels = []
label_file.seek(8)
for i in range(10):
    labels.append(int.from_bytes(label_file.read(1), byteorder='big'))

print(labels)
