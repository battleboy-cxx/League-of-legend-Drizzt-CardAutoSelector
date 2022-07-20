# This is a sample Python script.
import time

import pyautogui
import sys
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class cardmaster:
    mouse_pos = 0
    img1 = '1.jpg'
    img2 = '2.jpg'
    img3 = '3.jpg'
    img4 = '4.jpg'
    img5 = '5.jpg'
    img6 = '6.jpg'
    img7 = '7.jpg'
    img8 = '8.jpg'
    img9 = '9.jpg'
    img10 = '10.jpg'



    button_location = (0,0,0,0)
    buttonx = 0
    buttony = 0
    def __init__(self): # 重载构造函数
        mouse_pos = 0
        redcard_color = 0
        bluecard_color = 0
        yellowcard_color = 0

    def __del__(self): # 重载析构函数

        pass # 空操作

    def mouse_move(self,button_location):
        pyautogui.moveTo(button_location)

    def mouse_move(self,button_location):
        pyautogui.moveTo(button_location)


    def locate_button(self):
        loc = pyautogui.locateCenterOnScreen("icon_xx.png",
                                             region=(0, 0, sizex / 2, sizey / 10))  # region参数限制查找范围，加快查找速度
        pyautogui.moveTo(*loc, duration=0.5)  # 移动鼠标
        pyautogui.click(clicks=1)  # 点击

    def locate_yellowbutton(self):
        self.button_location = pyautogui.locateOnScreen(self.yellow_img)
        while(self.button_location == None):
            self.button_location = pyautogui.locateOnScreen(self.learnt_img)
            time.sleep(4)
            print(1)
        self.buttonx, self.buttony = pyautogui.center(self.button_location)
        print(self.button_location)

    def locate_bluebutton(self):
        self.button_location = pyautogui.locateOnScreen(self.learnt_img)
        while(self.button_location == None):
            self.button_location = pyautogui.locateOnScreen(self.learnt_img)
            time.sleep(4)
            print(1)
        self.buttonx, self.buttony = pyautogui.center(self.button_location)
        print(self.button_location)

    def locate_redbutton(self):
        self.button_location = pyautogui.locateOnScreen(self.red_img)
        while(self.button_location == None):
            self.button_location = pyautogui.locateOnScreen(self.learnt_img)
            time.sleep(4)
            print(1)
        self.buttonx, self.buttony = pyautogui.center(self.button_location)
        print(self.button_location)

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #
    # pyautogui.alert('切牌启动')
    # time.sleep(2)
    # id = cardmaster()
    # id.locate_button()
    # print(pyautogui.size())
    # print(pyautogui.position())
    # id.mouse_move(button_location=id.button_location)
    #
    #



