# coding=utf-8
# ------------------------------------------------------------------------------
# 类 zprint
# ------------------------------------------------------------------------------
# 变更履历：
# 2020-01-06 | Zou Mingzhe   | Ver0.1  | 初始版本
# ------------------------------------------------------------------------------
# MAP：
# 已测试 | flush(self)                  | 返回计时时间
# ------------------------------------------------------------------------------
# Reference：
# https://en.wikipedia.org/wiki/ANSI_escape_code
# ------------------------------------------------------------------------------
from colorama import init as colorinit
# ------------------------------------------------------------------------------
CSI = '\033['
OSC = '\033]'
BEL = '\007'

class AnsiStyle():
    """
    style :
        0   重置、清除样式   Reset / Normal
        1   加粗            Bold or increased intensity
        2                   Faint or decreased intensity
        3   斜体            Italic
        4   下划线          Underline
        5   闪烁            Slow Blink
        6   闪烁            Rapid Blink
        7   反显            Reverse video
        8   隐藏            Conceal
        22  非粗体          Normal color or intensity
        24  非下划线        Underline off
        25  非闪烁          Blink off
        27  非反显          Reverse/invert off
    """
    reset           = CSI + "0m"
    bright          = CSI + "1m"
    dim             = CSI + "2m"
    normal          = CSI + "22m"
    underline       = CSI + "4m"
    underline_off   = CSI + "24m"
    blink           = CSI + "5m"
    blink_off       = CSI + "25m"
    reverse         = CSI + "7m"
    reverse_off     = CSI + "27m"

class AnsiFore():
    """
    foreground :
        黑色        30  black
        红色        31  red
        绿色        32  green
        黄色        33  yellow
        蓝色        34  blue
        品红色      35  magenta
        青色        36  cyan
        白色 (灰)   37  white
        亮黑色 (灰) 90
        亮红色      91
        亮绿色      92
        亮黄色      93
        亮蓝色      94
        亮品红色    95
        亮青色      96
        亮白色      97
    """
    black   = CSI + "30m"
    red     = CSI + "31m"
    green   = CSI + "32m"
    yellow  = CSI + "33m"
    blue    = CSI + "34m"
    magenta = CSI + "35m"
    cyan    = CSI + "36m"
    white   = CSI + "37m"

class AnsiBack():
    """
    background :
        黑色        40  black
        红色        41  red
        绿色        42  green
        黄色        43  yellow
        蓝色        44  blue
        品红色      45  magenta
        青色        46  cyan
        白色 (灰)   47  white
        亮黑色 (灰) 100
        亮红色      101
        亮绿色      102
        亮黄色      103
        亮蓝色      104
        亮品红色    105
        亮青色      106
        亮白色      107
    """
    black   = CSI + "40m"
    red     = CSI + "41m"
    green   = CSI + "42m"
    yellow  = CSI + "43m"
    blue    = CSI + "44m"
    magenta = CSI + "45m"
    cyan    = CSI + "46m"
    white   = CSI + "47m"
# ------------------------------------------------------------------------------
class zprint:
    """
    timeout类提供了计时和超时判断功能，它通过调用系统time模块来获取时间。
    """
    def __init__(self):
        # print("%s init"%(self.__class__.__name__))
        self.__version = "0.1"
        self.__string = ""
        colorinit(autoreset=True)
# ------------------------------------------------------------------------------
    @staticmethod
    def std(*args):
        """
        输出至std：
        输入参数：*args
        返回参数：无
        说明：调用该方法将string输出至std，该方法具有多线程并发控制。
        """
        string = ""
        for item in args:
            if string:
                string = string + " "
            if type(item) is not str:
                string = string + str(item)
            else:
                string = string + item
        if string:
            string = string + "\n"
            print(string, end="")
# ------------------------------------------------------------------------------
    def flush(self):
        """
        刷出缓冲区：
        输入参数：无
        返回参数：无
        说明：调用该方法将刷出缓冲区。
        """
        if self.__string:
            self.__string = self.__string + "\n"
            print(self.__string, end="")
            self.__string = ""
# ------------------------------------------------------------------------------
    def color(self, string, *args):
        """
        打印信息至缓冲区：
        输入参数：style 样式 fore 前景色 back 背景色
        返回参数：无
        说明：调用该方法将打印信息加入缓冲区。
        """
        if type(string) is not str:
            string = str(string)
        if args:
            cformat = ""
            for i in args:
                cformat = cformat + i
            cformat = cformat + string + AnsiStyle.reset
            self.__string = self.__string + cformat
        else:
            self.__string = self.__string + string
# ------------------------------------------------------------------------------
