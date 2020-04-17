#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
# 类 timeout
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2018-10-04 | Zou Mingzhe   | Ver0.2  | 1.修改（Modified）：Reset(self) return value
#            |               |         |   from self.__TimeStart to 0
#            |               |         | 2.更名（Rename  ）：TimeStart(self) -> GetTimeStart(self)
# 2018-09-05 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | Version(self, ...)           | 版本显示
# 已测试 | Time(self)                   | 返回计时时间
# 已测试 | Reset(self)                  | 重置计时
# 已测试 | Timeout(self, ...)           | 超时判断
# 已测试 | GetTimeStart(self)           | 返回开始计时时间
# ----------------------------------------------------------------------------------------------------
import time
# ----------------------------------------------------------------------------------------------------
class timeout:
    """
    timeout类提供了计时和超时判断功能，它通过调用系统time模块来获取时间。
    """
    def __init__(self):
        self.__version = "0.2"
        self.__TimeStart = None
# ----------------------------------------------------------------------------------------------------
    def Version(self, isShow = False):
        """
        版本显示：
        输入参数：isShow = False
        返回参数：self.__version
        说明：调用该方法将返回类的版本号，若isShow == True则会在屏幕上打印版本号。
        """
        if(isShow):
            print("[ztools]-[Timeout]-[vesion:%s]" % self.__version)
        return self.__version
# ----------------------------------------------------------------------------------------------------
    def Time(self):
        """
        返回计时时间：
        输入参数：无
        返回参数：time.clock() - self.__TimeStart/0
        说明：调用该方法将返回计时时间。
        若self.__TimeStart != None，则返回time.clock() - self.__TimeStart。
        若self.__TimeStart == None，则记录当前时间至self.__TimeStart，返回0。
        """
        if(self.__TimeStart != None):
            return time.clock() - self.__TimeStart
        else:
            self.__TimeStart = time.clock()
            return 0
# ----------------------------------------------------------------------------------------------------
    def Reset(self):
        """
        重置计时：
        输入参数：无
        返回参数：0
        说明：调用该方法将记录当前时间至self.__TimeStart，返回0。
        """
        self.__TimeStart = time.clock()
        return 0
# ----------------------------------------------------------------------------------------------------
    def Timeout(self, threshold):
        """
        超时判断：
        输入参数：threshold
        返回参数：True/False
        说明：调用该方法将进行超时判断。
        若self.__TimeStart != None，则将time.clock() - self.__TimeStart与threshold进行比较，
        若time.clock() - self.__TimeStart > threshold，返回True，否则返回False。
        若self.__TimeStart == None，则记录当前时间至self.__TimeStart，返回False。
        """
        if(self.__TimeStart != None):
            if(time.clock() - self.__TimeStart > threshold):
                return True
            else:
                return False
        else:
            self.__TimeStart = time.clock()
            return False
# ----------------------------------------------------------------------------------------------------
    def GetTimeStart(self):
        """
        返回开始计时时间：
        输入参数：无
        返回参数：self.__TimeStart
        说明：调用该方法将返回self.__TimeStart。
        """
        return self.__TimeStart
# ----------------------------------------------------------------------------------------------------
