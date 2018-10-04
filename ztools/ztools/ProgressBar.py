#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
# 类 ProgressBar
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2018-09-05 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# 代码说明：
# ProgressBar类提供了进度条字符串。
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | Version(self, ...)               | 版本显示
# 已测试 | PercentProgressBar(self, ...)    | 百分比进度条
# 已测试 | NumberProgressBar(self, ...)     | 数字进度条
# ----------------------------------------------------------------------------------------------------
class ProgressBar:
    def __init__(self):
        self.__version = "0.1"
        self.__progress = 0
        self.__progressbarlist = ['', '▏', '▎', '▍', '▌', '▋', '▊', '▉', '█', '█']
# ----------------------------------------------------------------------------------------------------
# 版本显示：
# 输入参数：isShow = False
# 返回参数：self.__version
# 说明：调用该方法将返回类的版本号，若isShow == True则会在屏幕上打印版本号。
    def Version(self, isShow = False): 
        if(isShow):
            print("[ztools]-[ProgressBar]-[vesion:%s]" % self.__version)
        return self.__version
# ----------------------------------------------------------------------------------------------------
# 百分比进度条：
# 输入参数：progress
# 返回参数：strprogressbar
# 说明：调用该方法将返回百分比进度条，百分比进度条 = 百分比 + 进度条。progress必须介于0至1之间。
    def PercentProgressBar(self, progress):
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
        return strprogressbar
# ----------------------------------------------------------------------------------------------------
# 数字进度条：
# 输入参数：Done, Sum
# 返回参数：strprogressbar
# 说明：调用该方法将返回数字进度条，数字进度条 = Done/Sum + 进度条。
# 其中，Done为已完成进度，Sum为总进度。
    def NumberProgressBar(self, Done, Sum):
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
        return strprogressbar
# ----------------------------------------------------------------------------------------------------