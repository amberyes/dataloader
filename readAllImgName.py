import os

'''
edited by zr
date:2017.05.27
'''

path = '/Volumes/Amber‘s HP/dataset/sky/datasets/skyfinder/skyfinder/skydinder/crop_train/'
f = open("/Volumes/Amber‘s HP/dataset/sky/datasets/skyfinder/skyfinder/skydinder/train.txt", 'w')

for pic in os.listdir(path):
    f.write(pic+';'+pic.split('_')[0] +'.png'+'\n')#+'_'+pic.split('_')[1]+'_'+pic.split('_')[2]+'_gtFine'+
f.close()