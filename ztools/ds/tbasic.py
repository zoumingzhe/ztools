# coding=utf-8
# ------------------------------------------------------------------------------
# 类 tbasicop
# ------------------------------------------------------------------------------
# 变更履历：
# 2020-04-16 | Zou Mingzhe   | Ver0.1  | 初始版本
# ------------------------------------------------------------------------------
# MAP：
# 已测试 | len(self, ...)               | 获取项个数
# ------------------------------------------------------------------------------
class tbasicop:
    """
    tbasicop 类提供了基础操作。
    """
    def __init__(self):
        self.__version = "0.1"
# ------------------------------------------------------------------------------
    def len(self):
        """
        获取项个数：
        输入参数：
        返回参数：
        说明：调用该方法将返回列表中项的个数。
        """
        return len(self._list)
# ------------------------------------------------------------------------------