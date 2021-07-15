#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
# 类 hash
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2020-12-04 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | md5(self, ...)               | 计算md5值
# 已测试 | sha1(self, ...)              | 计算sha1值
# ----------------------------------------------------------------------------------------------------
import hashlib
import os
# ----------------------------------------------------------------------------------------------------
class hash():
    """
    hash类提供了哈希值计算接口。
    """
# ----------------------------------------------------------------------------------------------------
    @staticmethod
    def __file(h, fp):
        """
        哈希计算：
        输入参数：fp 文件路径
        返回参数：
        说明：调用该方法将返回文件哈希计算值。
        """
        try:
            with open(fp, 'rb') as f:
                d = f.read(4096)
                while d:
                    h.update(d)
                    d = f.read(4096)
                f.close()
                return h.hexdigest()
        except:
            return None
# ----------------------------------------------------------------------------------------------------
    @staticmethod
    def md5(*args, **kwargs):
        """
        md5计算：
        输入参数：data 数据
        返回参数：
        说明：调用该方法将返回md5计算值。
        """
        if not args and not kwargs:
            return hashlib.md5()
        if 'file' in kwargs:
            f = kwargs['file']
            x = type(f)
            if x is str and os.path.isfile(f):
                return hash.__file(hashlib.md5(), f)
            if x is list or x is tuple:
                h = []
                for n in f:
                    h.append(hash.__file(hashlib.md5(), n))
                return h if x is list else tuple(h)
            return None
        if not args:
            return None
        h = []
        for data in args:
            if type(data) is not bytes:
                return None
            h.append(hashlib.md5(data).hexdigest())
        return h if len(h) > 1 else h[0]
# ----------------------------------------------------------------------------------------------------
    @staticmethod
    def sha1(*args, **kwargs):
        """
        sha1计算：
        输入参数：data 数据
        返回参数：
        说明：调用该方法将返回sha1计算值。
        """
        if not args and not kwargs:
            return hashlib.sha1()
        if 'file' in kwargs:
            f = kwargs['file']
            x = type(f)
            if x is str and os.path.isfile(f):
                return hash.__file(hashlib.sha1(), f)
            if x is list or x is tuple:
                h = []
                for n in f:
                    h.append(hash.__file(hashlib.sha1(), n))
                return h if x is list else tuple(h)
            return None
        if not args:
            return None
        h = []
        for data in args:
            if type(data) is not bytes:
                return None
            h.append(hashlib.sha1(data).hexdigest())
        return h if len(h) > 1 else h[0]
# ----------------------------------------------------------------------------------------------------
