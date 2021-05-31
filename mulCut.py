import os
import cv2
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
# 遍历指定目录，显示目录下的所有文件名
def CropImage4File(filepath,destpath):
    pathDir =  os.listdir(filepath)    # 列出文件路径中的所有路径或文件
    for allDir in pathDir:
        if allDir =='.DS_Store':
            continue
        child = os.path.join(filepath, allDir)
        dest = os.path.join(destpath,allDir)
        if os.path.isfile(child):
            image = Image.open(child) #cv2.imread(child)
            sp = image.size           #获取图像形状：返回【行数值，列数值】列表
            sz1 = sp[0]                 #图像的高度（行 范围）
            sz2 = sp[1]                 #图像的宽度（列 范围）
            #sz3 = sp[2]                #像素值由【RGB】三原色组成

            #你想对文件的操作
            a=int(sz1/2-259) # x start
            b=int(sz1/2+259) # x end
            c=int(sz2/2-100) # y start
            d=int(sz2/2+308) # y end
            cropImg = image.crop((a,c,b,d))  # (left, upper, right, lower)  #image[a:b,c:d]   #裁剪图像
            #cv2.imwrite(dest,cropImg)  #写入图像路径
            cropImg.save(dest)

if __name__ == '__main__':
    filepath ='/Volumes/Amber‘s HP/dataset/sky/datasets/skyfinder/skyfinder/75/'             #源图像
    destpath='/Volumes/Amber‘s HP/dataset/sky/datasets/skyfinder/skyfinder/train_75/'        # resized images saved here
    CropImage4File(filepath,destpath)

