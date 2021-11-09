# coding=utf-8
# ----------------------------------------------------------------------------------------------------
# 类 tstack
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2020-04-17 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | get(self, ...)               | 从堆栈顶取出一个项
# 已测试 | put(self, ...)               | 向堆栈顶添加一个项
# ----------------------------------------------------------------------------------------------------
from .tbasic import tbasicop
# ----------------------------------------------------------------------------------------------------
class tstack(tbasicop):
    """
    tstack 类提供了堆栈访问接口。
    """
    def __init__(self):
        self.__version = "0.1"
        self._list = []
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
