import os
import shutil
path = '/Volumes/Amber‘s HP/dataset/sky/datasets/cityscapes/gtFine_trainvaltest/gtFine/val/munster'
new_path ='/Volumes/Amber‘s HP/dataset/sky/datasets/city/gt'
for root, dirs, files in os.walk(path):
    for i in range(len(files)):
        if (files[i][-16:] == 'gtFine_color.png'):
            file_path = root + '/' + files[i]
            new_file_path = new_path + '/' + files[i]
            shutil.copy(file_path, new_file_path)



