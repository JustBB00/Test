# -*- coding:utf-8 -*-
import re
i = 0
Flag = 0
f = open('BaseLine.a2l','r')
f_new = open('new_file.a2l','w')


for line in f:
    i = i+1
    # 若包含 begin、MEASUREMENT和 . 分离出后缀
    if (line.find('begin') != -1) and (line.find('MEASUREMENT') != -1) and (line.find('.') != -1):
        #print line.split()
        #print line.split()[2]                   #提取到目标信号
        print line.split()[2].split('.')        #分离出后缀
        suffix = line.split()[2].split('.')[1]
        Flag = 1                                #开始检测标志位
        print '+++++++++++++++++++++++++'
    #
    
    if ((line.find('LINK_MAP') != -1) or (line.find('SYMBOL_LINK') != -1)) and (Flag == 1) and (line.find('.') == -1 ):
        i = 0                                   #截取Rte_Signal_id
        #print line.split('"')
        Temp = line.split('"')[1]
        #print line.split()[1]
        #print line.split()[1].split('"')
        SignalS = Temp.split()[0]
        Signal = SignalS + '.' + suffix
        print Signal
        line = line.split('"')[0] + '"' +Signal + '"' + line.split('"')[2]
        print '+++++++++++++++++++++++++'

    if (line.find('end') != -1) and (line.find('MEASUREMENT') != -1):
        Flag = 0
    f_new.write(line)


f.close()
f_new.close()

f = open('new_file.a2l','r')
f_new = open('BaseLine_new.a2l','w')

for line in f:
    i = i+1
    # 若包含 begin、MEASUREMENT和 . 分离出后缀
    if (line.find('begin') != -1) and (line.find('MEASUREMENT') != -1) and ((line.find('_VDx') != -1) or (line.find('_Objx') != -1)):
        #print line.split()
        #print line.split()[2]                   #提取到目标信号
        #print line.split()[2].split('.')        #不用分离出后缀
        print line.split()[2]
        suffix = '_0_'
        Flag = 1                                #开始检测标志位
        print '+++++++++++++++++++++++++'
    #
    
    if ((line.find('LINK_MAP') != -1) or (line.find('SYMBOL_LINK') != -1)) and (Flag == 1) and (line.find('.') == -1 ):
        i = 0                                   #截取Rte_Signal_id
        #print line.split('"')
        Temp = line.split('"')[1]
        #print line.split()[1]
        #print line.split()[1].split('"')
        SignalS = Temp.split()[0]
        Signal = SignalS + '.' + suffix
        print Signal
        line = line.split('"')[0] + '"' +Signal + '"' + line.split('"')[2]
        print '+++++++++++++++++++++++++'

    if (line.find('end') != -1) and (line.find('MEASUREMENT') != -1):
        Flag = 0
    f_new.write(line)

f.close()
f_new.close()
