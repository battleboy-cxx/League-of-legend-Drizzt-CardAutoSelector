import win32gui
import win32api
import win32con
import time
from config import *

def press_key(key):
    win32api.keybd_event(key, 0, 0, 0)
    win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)


def get_pixel_color(x, y):
    dc = win32gui.GetDC(0)
    color = win32gui.GetPixel(dc, x, y)
    win32gui.ReleaseDC(0, dc)
    return color


def press_blue_card():
    count = 0
    while True:
        if count > 5:
            break
        count += 1
        print(get_pixel_color(target_x, target_y))
        if get_pixel_color(target_x, target_y) == color_dict["default"]:
            press_key(0x57)  # "W"
            time.sleep(0.1)
            if get_pixel_color(target_x, target_y) == color_dict["blue"]:
                press_key(0x57)  # "W"
                break


def press_red_card():
    count = 0
    while True:
        if count > 5:
            break
        count += 1
        print(get_pixel_color(target_x, target_y))
        if get_pixel_color(target_x, target_y) == color_dict["default"]:
            press_key(0x57)  # "W"
            time.sleep(0.1)
            if get_pixel_color(target_x, target_y) == color_dict["red"]:
                press_key(0x57)  # "W"
                break


def press_yellow_card():
    print("press_yellow_card")
    count = 0
    while True:
        if count > 50:
            break
        count += 1
        print(get_pixel_color(target_x, target_y))
        if get_pixel_color(target_x, target_y) == color_dict["default"]:
            press_key(0x57)  # "W"
            time.sleep(0.1)
            if get_pixel_color(target_x, target_y) == color_dict["yellow"]:
                press_key(0x57)  # "W"
                break


def handle_hotkey(id):
    if id == 1:
        press_blue_card()
    elif id == 2:
        press_red_card()
    elif id == 3:
        press_yellow_card()


def main():
    # 请以管理员权限运行程序
    press_blue_card_hotkey = 0x31  # "1"
    press_red_card_hotkey = 0x32  # "2"
    press_yellow_card_hotkey = 0x33  # "3"
    win32gui.RegisterHotKey(None, 1, win32con.MOD_ALT, press_blue_card_hotkey)
    win32gui.RegisterHotKey(None, 2, win32con.MOD_ALT, press_red_card_hotkey)
    win32gui.RegisterHotKey(None, 3, win32con.MOD_ALT, press_yellow_card_hotkey)
    try:
        while True:
            msg = win32gui.GetMessage(None, 0, 0)
            if msg[1][1] == win32con.WM_HOTKEY:
                handle_hotkey(msg[1][2])
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()