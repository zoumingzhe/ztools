#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
# 类 hash
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2020-12-04 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | Version(self, ...)           | 版本显示
# 未测试 | md5(self, ...)               | 读
# ----------------------------------------------------------------------------------------------------
import hashlib
# ----------------------------------------------------------------------------------------------------
class hash():
    """
    hash类提供了对.xls文件的操作。
    """
    def __init__(self):
        self.__version = "0.1"
# ----------------------------------------------------------------------------------------------------
    def Version(self, isShow = False):
        """
        版本显示：
        输入参数：isShow = False
        返回参数：self.__version
        说明：调用该方法将返回类的版本号，若isShow == True则会在屏幕上打印版本号。
        """
        if(isShow):
            print("[ztools]-[hash]-[vesion:%s]" % self.__version)
        return self.__version
# ----------------------------------------------------------------------------------------------------
    def md5(self, data = None, encoding = None, filename = None):
        """
        md5计算：
        输入参数：data 数据
        返回参数：
        说明：调用该方法将。
        """
        x = type(data)
        if x is bytes:
            return hashlib.md5(data).hexdigest()
        elif x is str:
            return hashlib.md5(data.encode(encoding)).hexdigest()
        elif type(filename) is str:
            try:
                with open(filename, 'rb') as f:
                    h = hashlib.md5()
                    d = f.read(4096)
                    while d:
                        h.update(d)
                        d = f.read(4096)
                    f.close()
                    return h.hexdigest()
            except:
                return None
        else:
            return None
# ----------------------------------------------------------------------------------------------------
    def sha1(self, data = None, encoding = None, filename = None):
        """
        sha1计算：
        输入参数：data 数据
        返回参数：
        说明：调用该方法将。
        """
        x = type(data)
        if x is bytes:
            return hashlib.sha1(data).hexdigest()
        elif x is str:
            return hashlib.sha1(data.encode(encoding)).hexdigest()
        elif type(filename) is str:
            try:
                with open(filename, 'rb') as f:
                    h = hashlib.sha1()
                    d = f.read(4096)
                    while d:
                        h.update(d)
                        d = f.read(4096)
                    f.close()
                    return h.hexdigest()
            except:
                return None
        else:
            return None
# ----------------------------------------------------------------------------------------------------
