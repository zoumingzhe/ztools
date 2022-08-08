# coding=utf-8
# ------------------------------------------------------------------------------
# 类 hash
# ------------------------------------------------------------------------------
# 变更履历：
# 2020-12-04 | Zou Mingzhe   | Ver0.1  | 初始版本
# ------------------------------------------------------------------------------
# MAP：
# 已测试 | md5(self, ...)               | 计算md5值
# 已测试 | sha1(self, ...)              | 计算sha1值
# ------------------------------------------------------------------------------
import hashlib
import os
# ------------------------------------------------------------------------------
class hash():
    """
    hash类提供了哈希值计算接口。
    """
# ------------------------------------------------------------------------------
    @staticmethod
    def __file(h, filepath):
        """
        哈希计算：
        输入参数： filepath = <path> 文件路径
        返回参数：
        说明：调用该方法将返回文件哈希计算值。
        """
        with open(filepath, 'rb') as f:
            d = f.read(4096)
            while d:
                h.update(d)
                d = f.read(4096)
            f.close()
            return h.hexdigest()
# ------------------------------------------------------------------------------
    @staticmethod
    def __calc(handle, *args, **kwargs):
        """
        哈希计算：
        输入参数： filepath = <path> 文件路径
        返回参数：
        说明：调用该方法将返回哈希计算值。
        """
        if 'filepath' in kwargs:
            fp = kwargs.pop('filepath')
            if type(fp) is not str:
                raise TypeError('filepath must string')
            if not os.path.isfile(fp):
                raise ValueError('file "{}" is not exist'.format(fp))
            return hash.__file(handle, fp)
        # too many args
        assert len(args) == 1, 'too many arguments'
        # handle string type
        data = args[0]
        if type(data) is str:
            assert 'encode' in kwargs, 'miss encode param'
            data = data.encode(kwargs['encode'])
        assert type(data) is bytes, 'data must bytes'
        handle.update(data)
        return handle.hexdigest()
# ------------------------------------------------------------------------------
    @staticmethod
    def md5(*args, **kwargs):
        """
        md5计算：
        输入参数：
        返回参数：
        说明：调用该方法将返回md5计算值。
        """
        handle = hashlib.md5()
        if not args and not kwargs:
            return handle
        return hash.__calc(handle, *args, **kwargs)
# ------------------------------------------------------------------------------
    @staticmethod
    def sha1(*args, **kwargs):
        """
        sha1计算：
        输入参数：
        返回参数：
        说明：调用该方法将返回sha1计算值。
        """
        handle = hashlib.sha1()
        if not args and not kwargs:
            return handle
        return hash.__calc(handle, *args, **kwargs)
# ------------------------------------------------------------------------------
