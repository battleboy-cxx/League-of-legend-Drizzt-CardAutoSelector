import win32gui


def colorref2rgb(colorref):
    """
    转换 Windows GDI 颜色表示的 COLORREF 值为 RGB 值
    :param colorref: int 颜色表示的 COLORREF 值
    :return: tuple 表示 RGB 值的元组 (r, g, b)
    """
    red = colorref & 0xFF
    green = (colorref >> 8) & 0xFF
    blue = (colorref >> 16) & 0xFF
    return red, green, blue

def get_pixel_color(x, y):
    dc = win32gui.GetDC(0)
    colorref = win32gui.GetPixel(dc, x, y)
    win32gui.ReleaseDC(0, dc)
    return colorref2rgb(colorref)