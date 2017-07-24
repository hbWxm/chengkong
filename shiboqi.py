# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 23:28:29 2017

@author: wyl
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import math
import os
import sys
import visa
import time

plt.close()  # clf() # 清图  cla() # 清坐标轴 close() # 关窗口
fig = plt.figure(figsize=(50,50))
ax = fig.add_subplot(1, 1, 1)
ax.axis([0.0,10000.0, 0.0,100.0])  # 设置图像显示的时候XY轴比例
plt.grid(True)  # 添加网格
plt.ion()  # interactive mode on
#IniObsX = 0000
#IniObsY = 100
#IniObsAngle = 135
#IniObsSpeed = 10 * math.sqrt(2)  # 米/秒
print('开始仿真')
rm = visa.ResourceManager()
print (rm.list_resources())
instr = rm.open_resource('USB0::0x0699::0x0408::C029817::INSTR')
print (instr.query("*IDN?"))
instr.write(":DATa:SOUrce CH1")
instr.write(":DATa:STARt 1")
instr.write(":DATa:STOP 5000")
instr.write(":DATa:ENCdg ASCIi")
instr.write(":DATa:WIDth 1")
instr.write(":HEADer 1")
instr.write(":VERBose")
instr.write(":HEADer 0")
print(instr.query(":WFMOutpre?"))
tt = 0
obsX = range(5000)
try:
    while(1):
        # 障碍物船只轨迹

        wav = instr.query(":CURVe?")

        obsY = list(int(i) for i in wav.split(','))
        ax.scatter(obsX, obsY, c='b', marker='.')  # 散点图
        # ax.lines.pop(1)  删除轨迹
        # 下面的图,两船的距离
        plt.pause(0.0001)
        #plt.show()
        time.sleep(0.1)
        tt = tt+1
        #if (5==tt):

        plt.cla()
        tt = 0
except Exception as err:
    print(err)