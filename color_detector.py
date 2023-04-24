# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 13:58
# @Author  : Xiaxuan Chen
# @File    : Utils.color_detector.py
# @Description : 动态检测屏幕目标点颜色函数
import time

import pyscreeze
import win32gui
from PIL import ImageGrab
from config import *


def get_pixel_color(x, y):
    dc = win32gui.GetDC(0)
    color = win32gui.GetPixel(dc, x, y)
    win32gui.ReleaseDC(0, dc)
    return color


if __name__ == '__main__':
    last_color = 0
    while True:
        color = get_pixel_color(target_x, target_y)

        if color != last_color:
            print(color)

        last_color = color
        time.sleep(1)