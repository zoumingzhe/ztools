#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
# 类 File
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2019-04-29 | Zou Mingzhe   | Ver0.3  | 1.增加 map(self, key = None, path = None)
# 2019-04-20 | Zou Mingzhe   | Ver0.2  | 1.完善帮助信息
# 2019-04-14 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | Version(self, ...)  | 版本显示
# 未测试 | map(self, ...)      | 路径映射
# 已测试 | scan(self, ...)     | 扫描文件
# 未测试 | get_path(self, ...) | 获取路径
# 未测试 | get_name(self, ...) | 获取文件名
# 未测试 |get_folder(self, ...)| 获取文件夹名
# 已测试 | copy(self, ...)     | 拷贝文件
# 已测试 | move(self, ...)     | 移动文件
# 已测试 | delete(self, ...)   | 删除文件
# 未开发 | zip(self, ...)      | 压缩文件
# ----------------------------------------------------------------------------------------------------
import os
import shutil
# ----------------------------------------------------------------------------------------------------
class File:
    """
    File类提供了对文件访问的操作。
    """
    def __init__(self):
        self.__version = "0.3"
        self.__path = {}
# ----------------------------------------------------------------------------------------------------
    def Version(self, isShow = False):
        """
        版本显示：
        输入参数：isShow = False
        返回参数：self.__version
        说明：调用该方法将返回类的版本号，若isShow == True则会在屏幕上打印版本号。
        """
        if(isShow):
            print("[ztools]-[File]-[vesion:%s]" % self.__version)
        return self.__version
# ----------------------------------------------------------------------------------------------------
    def map(self, key = None, path = None):
        """
        路径映射：
        输入参数：
        返回参数：self.__path
        说明：调用该方法将记录路径映射。
        """
        if(key != None and path != None):
            self.__path[key] = path
        if(key != None and path == None):
            return self.__path[key]
        return self.__path
# ----------------------------------------------------------------------------------------------------
    def scan(self, directory, sub=False, prefix=None, postfix=None):
        info = []
        for root, sub_dirs, files in os.walk(directory):
            if sub == False:
                sub_dirs[:] = []
            for special_file in files:
                if postfix:
                    if special_file.endswith(postfix):
                        info.append(os.path.join(root,special_file))
                elif prefix:
                    if special_file.startswith(prefix):
                        info.append(os.path.join(root,special_file))
                else:
                    info.append(os.path.join(root,special_file))
        return info
# ----------------------------------------------------------------------------------------------------
    def a_folder(self, filepath):
        ffolder,fname=os.path.split(filepath)    #分离文件名和路径
        return ffolder
# ----------------------------------------------------------------------------------------------------
    def a_name(self, filepath):
        ffolder,fname=os.path.split(filepath)    #分离文件名和路径
        return fname
# ----------------------------------------------------------------------------------------------------
    def get_path(self, folder, name):
        path = []
        for i in range(len(name)):
            path.append(folder + '\\' + name[i])
        return path
# ----------------------------------------------------------------------------------------------------
    def get_name(self, filepath):
        name = []
        for i in range(len(filepath)):
            fpath,fname=os.path.split(filepath[i])    #分离文件名和路径
            name.append(fname)
        return name
# ----------------------------------------------------------------------------------------------------
    def get_folder(self, filepath):
        folder = []
        for i in range(len(filepath)):
            ffolder,fname=os.path.split(filepath[i])    #分离文件名和路径
            folder.append(ffolder)
        return folder
# ----------------------------------------------------------------------------------------------------
    def copy(self, srcfile, dstfile):
        """
        拷贝文件：
        输入参数：srcfile 源文件路径，dstfile 目的文件路径
        返回参数：
        说明：调用该方法将文件从源路径拷贝到目的路径。
        """
        if not os.path.isfile(srcfile):
            print("%s not exist!"%(srcfile))
        else:
            fpath,fname=os.path.split(dstfile)    #分离文件名和路径
            if not os.path.exists(fpath):
                os.makedirs(fpath)                #创建路径
            shutil.copyfile(srcfile,dstfile)      #复制文件
            print("copy %s -> %s"%( srcfile,dstfile))
# ----------------------------------------------------------------------------------------------------
    def move(self, srcfile, dstfile):
        """
        移动文件：
        输入参数：srcfile 源文件路径，dstfile 目的文件路径
        返回参数：
        说明：调用该方法将文件从源路径移动到目的路径。
        """
        if not os.path.isfile(srcfile):
            print("%s not exist!"%(srcfile))
        else:
            fpath,fname=os.path.split(dstfile)    #分离文件名和路径
            if not os.path.exists(fpath):
                os.makedirs(fpath)                #创建路径
            shutil.move(srcfile,dstfile)          #移动文件
            print("move %s -> %s"%( srcfile,dstfile))
# ----------------------------------------------------------------------------------------------------
    def delete(self, srcfile):
        """
        删除文件：
        输入参数：srcfile 源文件路径
        返回参数：
        说明：调用该方法将文件从源路径删除。
        """
        if not os.path.isfile(srcfile):
            print("%s not exist!"%(srcfile))
        else:
            os.remove(srcfile)
            print("delete %s"%( srcfile))
# ----------------------------------------------------------------------------------------------------
    def zip(self, srcfile):
        if not os.path.isfile(srcfile):
            print("%s not exist!"%(srcfile))
        else:
            shutil.make_archive(data_bak, "zip", srcfile)
# ----------------------------------------------------------------------------------------------------
