import os

import PIL.Image as Image

# ============1.打开图片============
file='/Volumes/Amber‘s HP/dataset/sky/datasets/city/gt'
for root, dirs, files in os.walk("/Volumes/Amber‘s HP/dataset/sky/datasets/city/gt"):
	print(root)  # 当前目录路径
	print(dirs)  # 当前路径下所有子目录
	print(files)
for x in files:
    path=x
    img = Image.open(('/Volumes/Amber‘s HP/dataset/sky/datasets/city/gt/'+x))
    img_array = img.load()
    # 遍历每一个像素块，并处理颜色
    width, height = img.size  # 获取宽度和高度
    for x in range(0, width):
        for y in range(0, height):
            rgb = img_array[x, y]  # 获取一个像素块的rgb
            r = rgb[0]
            g = rgb[1]
            b = rgb[2]

            if b >= 180 and b <= 190:  # 判断规则
                img_array[x, y] = (255, 255, 255)
            else:
                img_array[x, y] = (0, 0, 0)

    # ============3.保存图片============
    img.save("/Volumes/Amber‘s HP/dataset/sky/datasets/city/mod_gt/"+path)
'''
img = Image.open('/Volumes/Amber‘s HP/dataset/sky/datasets/city/aachen_000000_000019_gtFine.png')

# ============2.处理图片============
# 将图片分成小方块
img_array = img.load()
# 遍历每一个像素块，并处理颜色
width, height = img.size  # 获取宽度和高度
for x in range(0, width):
    for y in range(0, height):
        rgb = img_array[x, y]  # 获取一个像素块的rgb
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]

        if b>=180 and b<=190:  # 判断规则
            img_array[x, y] = (255, 255, 255)
        else:
            img_array[x, y] = (0, 0, 0)

# ============3.保存图片============
img.save("2.png")
'''