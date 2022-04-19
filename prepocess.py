import os
import random


trainval_percent = 0.9
train_percent = 0.9
xmlfilepath = 'D:\\Dataset\\PCB_dataset\\data\\Annotations'
txtsavepath = 'D:\\Dataset\\PCB_dataset\\data\\ImageSets'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('D:\\Dataset\\PCB_dataset\\data\\ImageSets\\trainval.txt', 'w')
ftest = open('D:\\Dataset\\PCB_dataset\\data\\ImageSets\\test.txt', 'w')
ftrain = open('D:\\Dataset\\PCB_dataset\\data\\ImageSets\\train.txt', 'w')
fval = open('D:\\Dataset\\PCB_dataset\\data\\ImageSets\\val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
