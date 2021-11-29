# coding=utf-8
# ------------------------------------------------------------------------------
# 类 timeout
# ------------------------------------------------------------------------------
# 变更履历：
# 2018-10-04 | Zou Mingzhe   | Ver0.2  | 1.修改（Modified）：reset(self) return value
#            |               |         |   from self.__start_time to 0
#            |               |         | 2.更名（Rename  ）：start_time(self) -> get_start_time(self)
# 2018-09-05 | Zou Mingzhe   | Ver0.1  | 初始版本
# ------------------------------------------------------------------------------
# MAP：
# 已测试 | time(self)                   | 返回计时时间
# 已测试 | reset(self)                  | 重置计时
# 已测试 | timeout(self, ...)           | 超时判断
# 已测试 | get_start_time(self)         | 返回开始计时时间
# ------------------------------------------------------------------------------
import time
# ------------------------------------------------------------------------------
class timeout:
    """
    timeout类提供了计时和超时判断功能，它通过调用系统time模块来获取时间。
    """
    def __init__(self):
        self.__version = "0.2"
        self.__start_time = None
# ------------------------------------------------------------------------------
    def time(self):
        """
        返回计时时间：
        输入参数：无
        返回参数：time.clock() - self.__start_time/0
        说明：调用该方法将返回计时时间。
        若self.__start_time != None，则返回time.clock() - self.__start_time。
        若self.__start_time == None，则记录当前时间至self.__start_time，返回0。
        """
        if(self.__start_time != None):
            return time.clock() - self.__start_time
        else:
            self.__start_time = time.clock()
            return 0
# ------------------------------------------------------------------------------
    def reset(self):
        """
        重置计时：
        输入参数：无
        返回参数：0
        说明：调用该方法将记录当前时间至self.__start_time，返回0。
        """
        self.__start_time = time.clock()
        return 0
# ------------------------------------------------------------------------------
    def timeout(self, threshold):
        """
        超时判断：
        输入参数：threshold
        返回参数：True/False
        说明：调用该方法将进行超时判断。
        若self.__start_time != None，则将time.clock() - self.__start_time与threshold进行比较，
        若time.clock() - self.__start_time > threshold，返回True，否则返回False。
        若self.__start_time == None，则记录当前时间至self.__start_time，返回False。
        """
        if(self.__start_time != None):
            if(time.clock() - self.__start_time > threshold):
                return True
            else:
                return False
        else:
            self.__start_time = time.clock()
            return False
# ------------------------------------------------------------------------------
    def get_start_time(self):
        """
        返回开始计时时间：
        输入参数：无
        返回参数：self.__start_time
        说明：调用该方法将返回self.__start_time。
        """
        return self.__start_time
# ------------------------------------------------------------------------------
