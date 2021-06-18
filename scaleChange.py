from PIL import Image
import os


def imageResize(input_path, output_path, scale):
    # 获取输入文件夹中的所有文件/夹，并改变工作空间
    files = os.listdir(input_path)
    os.chdir(input_path)
    # 判断输出文件夹是否存在，不存在则创建
    if (not os.path.exists(output_path)):
        os.makedirs(output_path)
    for file in files:
        if file == '.DS_Store':
            continue
        # 判断是否为文件，文件夹不操作
        if (os.path.isfile(file)):



            img = Image.open(file)
            width = int(img.size[0] * scale)
            height = int(img.size[1] * scale)
            img = img.resize((width, height), Image.ANTIALIAS)
            img.save(os.path.join(output_path,   file))

input_path='/Volumes/Amber‘s HP/dataset/sky/datasets/cvpr10Data/min_train/'
output_path='/Volumes/Amber‘s HP/dataset/sky/datasets/cvpr10Data/enbig/'
scale=2
imageResize(input_path,output_path,scale)