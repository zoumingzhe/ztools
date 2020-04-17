#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
# 类 base
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2020-04-16 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | len(self, ...)               | 获取项个数
# ----------------------------------------------------------------------------------------------------
class base:
    """
    base类提供了列访问。
    """
    def __init__(self):
        self.__version = "0.1"
# ----------------------------------------------------------------------------------------------------
    def len(self):
        """
        获取项个数：
        输入参数：
        返回参数：
        说明：调用该方法将返回列中项的个数。
        """
        return len(self._list)
# ----------------------------------------------------------------------------------------------------
# 类 queue
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2020-04-17 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | Version(self, ...)           | 版本显示
# 已测试 | get(self, ...)               | 从队列头取出一个项
# 已测试 | put(self, ...)               | 向队列尾添加一个项
# ----------------------------------------------------------------------------------------------------
class queue(base):
    """
    queue类提供了队列访问接口。
    """
    def __init__(self):
        self.__version = "0.1"
        self._list = []
# ----------------------------------------------------------------------------------------------------
    def Version(self, isShow = False):
        """
        版本显示：
        输入参数：isShow = False
        返回参数：self.__version
        说明：调用该方法将返回类的版本号，若isShow == True则会在屏幕上打印版本号。
        """
        if(isShow):
            print("[ztools]-[queue]-[vesion:%s]" % self.__version)
        return self.__version
# ----------------------------------------------------------------------------------------------------
    def get(self):
        """
        取项：
        输入参数：
        返回参数：item or None
        说明：调用该方法将从队列头取出一个项item，若队列为空返回None。
        """
        if (self.len() > 0):
            item = self._list.pop(0)
            return item
        else:
            return None
# ----------------------------------------------------------------------------------------------------
    def put(self, item):
        """
        添项：
        输入参数：item
        返回参数：
        说明：调用该方法将向队列尾添加一个项item。
        """
        self._list.append(item)
# ----------------------------------------------------------------------------------------------------
# 类 stack
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2020-04-17 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | Version(self, ...)           | 版本显示
# 已测试 | get(self, ...)               | 从堆栈顶取出一个项
# 已测试 | put(self, ...)               | 向堆栈顶添加一个项
# ----------------------------------------------------------------------------------------------------
class stack(base):
    """
    stack类提供了堆栈访问接口。
    """
    def __init__(self):
        self.__version = "0.1"
        self._list = []
# ----------------------------------------------------------------------------------------------------
    def Version(self, isShow = False):
        """
        版本显示：
        输入参数：isShow = False
        返回参数：self.__version
        说明：调用该方法将返回类的版本号，若isShow == True则会在屏幕上打印版本号。
        """
        if(isShow):
            print("[ztools]-[stack]-[vesion:%s]" % self.__version)
        return self.__version
# ----------------------------------------------------------------------------------------------------
    def get(self):
        """
        取项：
        输入参数：
        返回参数：item or None
        说明：调用该方法将从堆栈顶取出一个项item，若堆栈为空返回None。
        """
        if (self.len() > 0):
            item = self._list.pop()
            return item
        else:
            return None
# ----------------------------------------------------------------------------------------------------
    def put(self, item):
        """
        添项：
        输入参数：item
        返回参数：
        说明：调用该方法将向堆栈顶添加一个项item。
        """
        self._list.append(item)
# ----------------------------------------------------------------------------------------------------
