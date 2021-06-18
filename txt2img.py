#!/usr/bin/env python
import os
from PIL import Image
import numpy as np
import random
def txt2img(path,mod_path):
    x=240
    y=320
    b=0
    c = Image.new("RGB",(x,y))
    f = open(path)

    lines = f.readlines()

    for line in lines:
        a=0
        for i in line.split(' '):
            #print(i)
            if i=='0':
                #print(255)
                c.putpixel([a,b],(255,255,255))
            elif i=='1':
                #print(0)
                c.putpixel([a,b],(0,0,0))
            a=a+1

        b=b+1
    c.save(mod_path)

file='/Volumes/Amber‘s HP/dataset/sky/datasets/cvpr10Data/label/'
mod_file='/Volumes/Amber‘s HP/dataset/sky/datasets/cvpr10Data/mod_label/'
path= os.listdir(file)
#print(path)
for i in path:
    txt2img(file+i,mod_file+i[:-4]+'.png')



