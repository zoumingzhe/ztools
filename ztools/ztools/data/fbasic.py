#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
# 类 filebase
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2019-05-24 | Zou Mingzhe   | Ver0.6  | 1.增加 archive(self, srcdir, dstdir = None, name = None, format = "zip")
#            |               |         | 2.增加 archive_unpack(self, srcpath, dstpath = None)
#            |               |         | 3.测试以上2个函数，完善函数帮助信息
# 2019-05-23 | Zou Mingzhe   | Ver0.5  | 1.修改 get_path(self, folder, name)  输入支持单str或list
#            |               |         | 2.修改 get_name(self, filepath)      输入支持单str或list
#            |               |         | 3.修改 get_folder(self, filepath)    输入支持单str或list
#            |               |         | 4.测试以上3个函数，完善函数帮助信息
# 2019-04-30 | Zou Mingzhe   | Ver0.4  | 1.增加 ensure(self, path, isCreate = True)
# 2019-04-29 | Zou Mingzhe   | Ver0.3  | 1.增加 map(self, key = None, path = None)
# 2019-04-20 | Zou Mingzhe   | Ver0.2  | 1.完善帮助信息
# 2019-04-14 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | Version(self, ...)           | 版本显示
# 已测试 | map(self, ...)               | 路径映射
# 已测试 | ensure(self, ...)            | 路径检查
# 已测试 | get_path(self, ...)          | 获取路径
# 已测试 | get_name(self, ...)          | 获取文件名
# 已测试 | get_folder(self, ...)        | 获取文件夹名
# 已测试 | scan(self, ...)              | 扫描文件
# 已测试 | copy(self, ...)              | 拷贝文件
# 已测试 | move(self, ...)              | 移动文件
# 已测试 | delete(self, ...)            | 删除文件
# 已测试 | archive(self, ...)           | 归档文件
# 已测试 | archive_unpack(self, ...)    | 归档文件释放
# 未开发 | zip(self, ...)               | 压缩文件
# ----------------------------------------------------------------------------------------------------
import os
import shutil
# ----------------------------------------------------------------------------------------------------
class fbasic:
    """
    filebase类提供了对文件访问的操作。
    """
    def __init__(self):
        self.__version = "0.6"
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
            print("[ztools]-[filebase]-[vesion:%s]" % self.__version)
        return self.__version
# ----------------------------------------------------------------------------------------------------
    def map(self, key = None, path = None):
        """
        路径映射：
        输入参数：key, path
        返回参数：self.__path
        说明：该方法提供路径映射的记录，
        若key、path均不为None则记录路径映射，
        若只有key不为None则返回key的路径映射，
        若key、path均为None则返回所有的的路径映射。
        """
        if(key != None and path != None):
            self.__path[key] = path
        if(key != None and path == None):
            return self.__path[key] # TODO：检查key是否在dict内
        return self.__path
# ----------------------------------------------------------------------------------------------------
    def ensure(self, path, isCreate = True):
        """
        路径检查：
        输入参数：path, isCreate = True
        返回参数：
        说明：该方法检查路径path是否存在并返回，若不存在则根据iscreate指示生成路径。
        """
        if os.path.exists(path) == False and isCreate == True:
            os.makedirs(path)
        return os.path.exists(path)
# ----------------------------------------------------------------------------------------------------
    def get_path(self, folder, name):
        """
        获取路径：
        输入参数：folder, name
        返回参数：path
        说明：该方法生成文件路径，folder指定文件夹路径，name指定文件名（支持list）。
        """
        if type(name) == list:
            path = []
            for i in range(len(name)):
                path.append(folder + '\\' + name[i])
            return path
        else:
            return (folder + '\\' + name)
# ----------------------------------------------------------------------------------------------------
    def get_name(self, filepath):
        """
        获取文件名：
        输入参数：filepath
        返回参数：name
        说明：该方法提取路径中的文件名，filepath指定文件路径（支持list）；若是文件夹路径则返回文件夹名。
        """
        if type(filepath) == list:
            name = []
            for i in range(len(filepath)):
                name.append(os.path.basename(filepath[i]))
            return name
        else:
            return os.path.basename(filepath)    #分离文件名和路径
# ----------------------------------------------------------------------------------------------------
    def get_folder(self, filepath):
        """
        获取文件夹名：
        输入参数：filepath
        返回参数：folder
        说明：该方法提取路径中的文件夹名，filepath指定文件路径（支持list）；若是文件夹路径则返回上一级问价夹路径。
        """
        if type(filepath) == list:
            folder = []
            for i in range(len(filepath)):
                folder.append(os.path.dirname(filepath[i]))
            return folder
        else:
            return os.path.dirname(filepath)    #分离文件名和路径
# ----------------------------------------------------------------------------------------------------
    def scan(self, directory, sub=False, prefix=None, postfix=None):
        """
        扫描文件：
        输入参数：directory, sub=False, prefix=None, postfix=None
        返回参数：info
        说明：该方法在指定目录（directory）下进行文件扫描，
        参数sub指定是否对子目录扫描（默认不扫描），
        参数prefix、postfix分别指定文件名的前缀和后缀。
        """
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
            fpath=os.path.dirname(dstfile)    #分离文件名和路径
            if not os.path.exists(fpath):
                os.makedirs(fpath)                #创建路径
            shutil.copyfile(srcfile,dstfile)      #复制文件
            print(" copy %s \r\n to-> %s" % ( srcfile, dstfile ) )
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
            fpath=os.path.dirname(dstfile)    #分离文件名和路径
            if not os.path.exists(fpath):
                os.makedirs(fpath)                #创建路径
            shutil.move(srcfile,dstfile)          #移动文件
            print(" move %s \r\n to-> %s" % ( srcfile, dstfile ) )
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
    def archive(self, srcdir, dstdir = None, buname = None, format = "zip"):
        """
        归档文件：
        输入参数：srcdir          需要归档的文件路径
                 dstdir = None   归档路径，不包括文件名，不指定时默认归档到同级文件夹下
                 buname = None   归档文件名，不包含后缀，不指定时默认使用“backup_文件夹名”作为文件名
                 format = "zip"  归档格式（zip、tar、bztar、gztar），默认使用zip
        返回参数：
        说明：调用该方法将文件归档至指定目录下。
        """
        if not os.path.exists(srcdir):
            print("%s not exist!"%(srcdir))
        else:
            if buname == None:
                buname = "backup_" + self.get_name(srcdir)
            if dstdir == None:
                dstdir = self.get_folder(srcdir)
            self.ensure(dstdir)
            dstdir = self.get_path(dstdir, buname)
            shutil.make_archive(dstdir, format, srcdir)
# ----------------------------------------------------------------------------------------------------
    def archive_unpack(self, srcpath, dstpath = None):
        """
        归档文件释放：
        输入参数：srcpath          需要释放的归档文件路径，包含文件名及后缀
                 dstpath = None   释放路径，不指定时默认释放到同级文件夹下
        返回参数：
        说明：调用该方法将归档文件释放至指定目录下。
        """
        if not os.path.isfile(srcpath):
            print("%s not exist!"%(srcpath))
        else:
            if dstpath == None:
                dstpath = self.get_folder(srcpath)
            shutil.unpack_archive(srcpath, dstpath)
# ----------------------------------------------------------------------------------------------------
