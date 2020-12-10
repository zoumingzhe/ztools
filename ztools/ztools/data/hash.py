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
# 已测试 | md5(self, ...)               | 计算md5值
# 已测试 | sha1(self, ...)              | 计算sha1值
# ----------------------------------------------------------------------------------------------------
import hashlib
# ----------------------------------------------------------------------------------------------------
class hash():
    """
    hash类提供了哈希值计算接口。
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
    def __file_md5(self, filename):
        """
        md5计算：
        输入参数：filename 文件名
        返回参数：
        说明：调用该方法将返回文件md5计算值。
        """
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
# ----------------------------------------------------------------------------------------------------
    def md5(self, *args, **kwargs):
        """
        md5计算：
        输入参数：data 数据
        返回参数：
        说明：调用该方法将返回md5计算值。
        """
        if not args and not kwargs:
            return hashlib.md5()
        if 'filename' in kwargs:
            filename = kwargs['filename']
            x = type(filename)
            if x is str:
                return self.__file_md5(filename)
            if x is list or x is tuple:
                h = []
                for name in filename:
                    h.append(self.__file_md5(name))
                if x is tuple:
                    h = tuple(h)
                return h
        encoding = None
        if 'encoding' in kwargs:
            encoding = kwargs['encoding']
        for data in args:
            x = type(data)
            if x is bytes:
                return hashlib.md5(data).hexdigest()
            elif x is str:
                return hashlib.md5(data.encode(encoding)).hexdigest()
        return None
# ----------------------------------------------------------------------------------------------------
    def __file_sha1(self, filename):
        """
        sha1计算：
        输入参数：filename 文件名
        返回参数：
        说明：调用该方法将返回文件sha1计算值。
        """
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
# ----------------------------------------------------------------------------------------------------
    def sha1(self, *args, **kwargs):
        """
        sha1计算：
        输入参数：data 数据
        返回参数：
        说明：调用该方法将返回sha1计算值。
        """
        if not args and not kwargs:
            return hashlib.sha1()
        if 'filename' in kwargs:
            filename = kwargs['filename']
            x = type(filename)
            if x is str:
                return self.__file_sha1(filename)
            if x is list or x is tuple:
                h = []
                for name in filename:
                    h.append(self.__file_sha1(name))
                if x is tuple:
                    h = tuple(h)
                return h
        encoding = None
        if 'encoding' in kwargs:
            encoding = kwargs['encoding']
        for data in args:
            x = type(data)
            if x is bytes:
                return hashlib.sha1(data).hexdigest()
            elif x is str:
                return hashlib.sha1(data.encode(encoding)).hexdigest()
        return None
# ----------------------------------------------------------------------------------------------------
