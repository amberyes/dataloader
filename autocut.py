from PIL import Image
import matplotlib.pyplot as plt
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os

files = []
for root, dirs, files in os.walk("/Volumes/Amber‘s HP/dataset/sky/datasets/skyfinder/images/9291"):
	print(root)  # 当前目录路径
	print(dirs)  # 当前路径下所有子目录
	print(files)
	
for x in files:
	path=x
#	if '/Volumes/Amber‘s HP/dataset/sky/datasets/skyfinder/images/9708/'+x ==  '/Volumes/Amber‘s HP/dataset/sky/datasets/skyfinder/images/9708/.DS_Store':
	#		continue
	# rest of your program
	im=Image.open('/Volumes/Amber‘s HP/dataset/sky/datasets/skyfinder/images/9291/'+x)  #打开图像
	
	# 图片的宽度和高度
	img_size = im.size
	print("图片宽度和高度分别是{}".format(img_size))
	"""
	裁剪：传入一个元组作为参数
	元组里的元素分别是：（距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
	"""
	# 截取图片中一块宽和高都是250的
	x = 0
	y = 0
	w = 240
	h = 240
	region = im.crop((x, y, x + w, y + h))
	region.save("/Volumes/Amber‘s HP/dataset/sky/datasets/skyfinder/deal/9291/"+path)
'''
im = Image.open('/Volumes/Amber‘s HP/dataset/sky/datasets/skyfinder/imagesdel/3297co/20130101_210123.jpg' )  # 打开图像

# 图片的宽度和高度
img_size = im.size
print("图片宽度和高度分别是{}".format(img_size))
"""
裁剪：传入一个元组作为参数
元组里的元素分别是：（距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
"""
# 截取图片中一块宽和高都是250的
x = 0
y = 0
w = 550
h = 380
region = im.crop((x, y, x + w, y + h))
region.save("./crop_test1.jpeg" )
'''

