import os
import re
import sys

path= r"/Volumes/Amber‘s HP/dataset/sky/datasets/city/gt"
fileList = os.listdir(path)
os.chdir(path)
for fileName in fileList:
    if fileName=='.DS_Store':
        continue
    path1 = r"/Volumes/Amber‘s HP/dataset/sky/datasets/city/gt/"+fileName

    fileList1 = os.listdir(path)  # 待修改文件夹
    print("修改前：" + str(fileList1))  # 输出文件夹中包含的文件
    os.chdir(path)  # 将当前工作目录修改为待修改文件夹的位置
    num =fileName  # 名称变量
    #i=0
    if fileName[:-10] != 'gtFine.png':

        pat = ".+\.(jpg|jpeg|JPG|png)"  # 匹配文件名正则表达式
        pattern = re.findall(pat, fileName)  # 进行匹配
        print('pattern[0]:', pattern)
        print('filename',fileName)
        print('num：', num) #, 'i:', i
        print(pattern[0])
        os.rename(fileName, (fileName.split('_')[0] +'_'+fileName.split('_')[1]+'_'+fileName.split('_')[2]+'_gtFine'+'.'+pattern[0]))  # 文件重新命名
            #i = i + 1  # 改变编号，继续下一项
print("---------------------------------------------------")
sys.stdin.flush()  # 刷新
print("修改后：" + str(os.listdir(path)))  # 输出修改后文件夹中包含的文件