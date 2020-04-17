#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
# 类 progressbar
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2019-05-03 | Zou Mingzhe   | Ver0.2  | 1.增加 EOF(self, isClean = False)
#            |               |         | 2.修改 PercentProgressBar(self, ...) 为 Percent(self, ...)
#            |               |         | 3.修改 NumberProgressBar(self, ...)  为 Number(self, ...)
# 2018-09-05 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | Version(self, ...)           | 版本显示
# 已测试 | Percent(self, ...)           | 百分比进度条
# 已测试 | Number(self, ...)            | 数字进度条
# 已测试 | EOF(self, ...)               | 结束符
# ----------------------------------------------------------------------------------------------------
import sys
# ----------------------------------------------------------------------------------------------------
class progressbar:
    """
    progressbar类提供了进度条字符串。
    """
    def __init__(self):
        self.__version = "0.2"
        self.__progress = 0
        self.__maxlength = 0
        self.__progressbarlist = ['', '▏', '▎', '▍', '▌', '▋', '▊', '▉', '█', '█']
# ----------------------------------------------------------------------------------------------------
    def Version(self, isShow = False):
        """
        版本显示：
        输入参数：isShow = False
        返回参数：self.__version
        说明：调用该方法将返回类的版本号，若isShow == True则会在屏幕上打印版本号。
        """
        if(isShow):
            print("[ztools]-[progressbar]-[vesion:%s]" % self.__version)
        return self.__version
# ----------------------------------------------------------------------------------------------------
    def Percent(self, progress, isShow = False):
        """
        百分比进度条：
        输入参数：progress, isShow = False
        返回参数：strprogressbar
        说明：调用该方法将返回百分比进度条，百分比进度条 = 百分比 + 进度条。progress必须介于0至1之间。
        """
        progress = progress * 100
        if(progress > 100):
            progress = 100
        elif(progress < 0):
            progress = 0        
        strprogressbar = str('%.2f%% ' % progress)
        self.__progress = progress
        for n in range(int(progress / 10)):
            strprogressbar = strprogressbar + '█'
        strprogressbar = strprogressbar + self.__progressbarlist[int(progress) % 10]
        self.__maxlength = max(len(strprogressbar), self.__maxlength)
        if(isShow):
            sys.stdout.write(strprogressbar + '\r')
            sys.stdout.flush()
        return strprogressbar
# ----------------------------------------------------------------------------------------------------
    def Number(self, Done, Sum, isShow = False):
        """
        数字进度条：
        输入参数：Done, Sum, isShow = False
        返回参数：strprogressbar
        说明：调用该方法将返回数字进度条，数字进度条 = Done/Sum + 进度条。
        其中，Done为已完成进度，Sum为总进度。
        """
        if(Sum <= 0):
            Sum = 1
        if(Done < 0):
            Done = 0
        if(Done > Sum):
            Done = Sum
        progress = Done * 100 / Sum
        if(progress > 100):
            progress = 100
        elif(progress < 0):
            progress = 0        
        strprogressbar = str('%d/%d ' % (Done, Sum))
        self.__progress = progress
        for n in range(int(progress / 10)):
            strprogressbar = strprogressbar + '█'
        strprogressbar = strprogressbar + self.__progressbarlist[int(progress) % 10]
        self.__maxlength = max(len(strprogressbar), self.__maxlength)
        if(isShow):
            sys.stdout.write(strprogressbar + '\r')
            sys.stdout.flush()
        return strprogressbar
# ----------------------------------------------------------------------------------------------------
    def EOF(self, isClean = False):
        """
        结束符：
        输入参数：isClean = False
        返回参数：
        说明：调用该方法将换行或清空屏幕进度条。
        """
        if(isClean):
            for n in range(self.__maxlength):
                sys.stdout.write(' ')
                sys.stdout.flush()
            sys.stdout.write('\r')
            sys.stdout.flush()
        else:
            sys.stdout.write('\n')
            sys.stdout.flush()
        self.__maxlength = 0
# ----------------------------------------------------------------------------------------------------
