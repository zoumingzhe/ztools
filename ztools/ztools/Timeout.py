#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
# 类 Timeout
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2018-09-05 | 邹明哲   | V0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# 代码说明：
# Timeout类提供了计时和超时判断功能，它通过调用系统time模块来获取时间。
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | Version(self, ...)  | 版本显示
# 已测试 | Reset(self)         | 重置计时
# 已测试 | Time(self)          | 返回计时时间
# 已测试 | Timeout(self, ...)  | 超时判断
# 已测试 | TimeStart(self)     | 返回开始计时时间
# ----------------------------------------------------------------------------------------------------
import time
# ----------------------------------------------------------------------------------------------------
class Timeout:
    def __init__(self):
        self.__version = "0.1"
        self.__TimeStart = None
# ----------------------------------------------------------------------------------------------------
# 版本显示：
# 输入参数：isShow = False
# 返回参数：self.__version
# 说明：调用该方法将返回类的版本号，若isShow == True则会在屏幕上打印版本号。
    def Version(self, isShow = False): 
        if(isShow):
            print("[library]-[Tools_Timeout]-[vesion:%s]" % self.__version)
        return self.__version
# ----------------------------------------------------------------------------------------------------
# 重置计时：
# 输入参数：无
# 返回参数：self.__TimeStart
# 说明：调用该方法将记录当前时间至self.__TimeStart，并返回self.__TimeStart。
    def Reset(self):
        self.__TimeStart = time.clock()
        return self.__TimeStart
# ----------------------------------------------------------------------------------------------------
# 返回计时时间：
# 输入参数：无
# 返回参数：self.__version
# 说明：调用该方法将返回计时时间。
# 若self.__TimeStart != None，则返回time.clock() - self.__TimeStart。
# 若self.__TimeStart == None，则记录当前时间至self.__TimeStart，返回0。
    def Time(self):
        if(self.__TimeStart != None):
            return time.clock() - self.__TimeStart
        else:
            self.__TimeStart = time.clock()
            return 0
# ----------------------------------------------------------------------------------------------------
# 超时判断：
# 输入参数：threshold
# 返回参数：True/False
# 说明：调用该方法将进行超时判断。
# 若self.__TimeStart != None，则将time.clock() - self.__TimeStart与threshold进行比较，
# 若time.clock() - self.__TimeStart > threshold，返回True，否则返回False。
# 若self.__TimeStart == None，则记录当前时间至self.__TimeStart，返回False。
    def Timeout(self, threshold):
        if(self.__TimeStart != None):
            if(time.clock() - self.__TimeStart > threshold):
                return True
            else:
                return False
        else:
            self.__TimeStart = time.clock()
            return False
# ----------------------------------------------------------------------------------------------------
# 返回开始计时时间：
# 输入参数：无
# 返回参数：self.__TimeStart
# 说明：调用该方法将返回self.__TimeStart。
    def TimeStart(self):
        return self.__TimeStart
# ----------------------------------------------------------------------------------------------------
