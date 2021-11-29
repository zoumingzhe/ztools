# coding=utf-8
import os
# ------------------------------------------------------------------------------
# 类 gitrepo
# ------------------------------------------------------------------------------
# 变更履历：
# 2021-11-25 | Zou Mingzhe   | Ver0.1  | 初始版本
# ------------------------------------------------------------------------------
# MAP：
# 已测试 | clone(self, ...)             | 克隆仓库
# ------------------------------------------------------------------------------
from git import Repo
# ------------------------------------------------------------------------------
class gitrepo:
    """
    gitrepo 类提供了git.Repo的二次封装，以简化常用git调用。
    """
# ------------------------------------------------------------------------------
    def __init__(self, path, url = None, branch = None):
        print('__init__')
        self.__version = "0.1"
        if not os.path.exists(path) or not os.listdir(path):
            assert url is not None, 'Missing URL parameter'
            self.__repo = Repo(path, url, branch)
        else:
            self.__repo = Repo(path)
        if url:
            for _url in self.__repo.remote().urls:
                assert _url == url, 'remote "{}" is not "{}"'.format(url, _url)
        if not branch:
            branch = 'master'
        _head = self.__repo.head.reference
        assert _head == branch, 'head "{}" is not "{}"'.format(_head, branch)
# ------------------------------------------------------------------------------
    def __enter__(self):
        return self
# ------------------------------------------------------------------------------
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
# ------------------------------------------------------------------------------
    @staticmethod
    def clone(path, url, branch = None):
        """
        克隆仓库：
        输入参数：
            - path：本地存储目录，必须为空
            - url：远程仓库url
            - branch（可选）：分支
        返回参数：git.Repo
        说明：该方法克隆远程仓库到本地存储目录，存储目录必须为空。
        """
        if not os.path.exists(path):
            os.makedirs(path)
        assert not os.listdir(path), 'The path must be an empty directory'
        multi_options = []
        if branch:
            opt_branch = '-b {}'.format(branch)
            multi_options.append(opt_branch)
        return Repo.clone_from(url, path, None, None, multi_options)
# ------------------------------------------------------------------------------
