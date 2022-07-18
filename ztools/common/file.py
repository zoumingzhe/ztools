# coding=utf-8
# ------------------------------------------------------------------------------
# 类 fbasic
# ------------------------------------------------------------------------------
# 变更履历：
# 2022-07-14 | Zou Mingzhe   | Ver0.9  | 1.增加 split(srcpath, dstdir = None, ...)
# 2021-10-20 | Zou Mingzhe   | Ver0.8  | 1.重构代码
# 2021-06-16 | Zou Mingzhe   | Ver0.7  | 1.修改 scan(self, ...) 支持扫描目录，返回元组并且有序
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
# ------------------------------------------------------------------------------
# MAP：
# 已测试 | map(self, ...)               | 路径映射
# 待修改 | ensure(self, ...)            | 路径检查
# 已测试 | join(self, ...)              | 拼接路径
# 已测试 | basename(self, ...)          | 获取文件名或文件夹名
# 已测试 | dirname(self, ...)           | 获取上一级路径
# 待重构 | scan(self, ...)              | 扫描文件夹
# 已测试 | copy(self, ...)              | 拷贝文件或文件夹
# 已测试 | move(self, ...)              | 移动文件或文件夹
# 已测试 | remove(self, ...)            | 删除文件或文件夹
# 已测试 | rename(self, ...)            | 重命名文件或文件夹
# 已测试 | archive(self, ...)           | 文件归档
# 已测试 | archive_unpack(self, ...)    | 归档文件解包
# 待测试 | split(self, ...)             | 文件分片
# 未开发 | zip(self, ...)               | 压缩文件
# ------------------------------------------------------------------------------
import os
import shutil
# ------------------------------------------------------------------------------
class fbasic:
    """
    filebase类提供了对文件访问的操作。
    """
    def __init__(self):
        self.__version = "0.9"
        self.__mappath = {}
# ------------------------------------------------------------------------------
    def map(self, key = None, path = None):
        """
        路径映射：
        输入参数：key, path
        返回参数：self.__mappath
        说明：该方法提供路径映射的记录，
        若key、path均不为None则记录路径映射，
        若只有key不为None则返回key的路径映射，
        若key、path均为None则返回所有的的路径映射。
        """
        if key is not None:
            if path is not None:
                self.__mappath[key] = path
            # TODO：检查key是否在dict内
            if key not in self.__mappath:
                return None
            return self.__mappath[key]
        return self.__mappath
# ------------------------------------------------------------------------------
    @staticmethod
    def ensure(path, isCreate = True):
        """
        路径检查：
        输入参数：path, isCreate = True
        返回参数：
        说明：该方法检查路径path是否存在并返回，若不存在则根据iscreate指示生成路径。
        """
        # TODO : remove isCreate para
        if os.path.exists(path) == False and isCreate == True:
            os.makedirs(path)
        return os.path.exists(path)
# ------------------------------------------------------------------------------
    @staticmethod
    def join(*args, **kwargs):
        """
        获取路径：
        输入参数：dirname, basename
        返回参数：path
        说明：该方法生成文件路径，dirname指定文件夹路径，basename指定文件名（支持list）。
        """
        if 'dirname' in kwargs:
            dirname = kwargs.pop('dirname')
            num = len(args)
            if num > 1:
                path = []
                for i in args:
                    path.append(os.path.join(dirname, i))
                return tuple(path)
            elif len(args) == 1:
                return os.path.join(dirname, args[0])
            else:
                return dirname
        else:
            return os.path.join(*args)
# ------------------------------------------------------------------------------
    @staticmethod
    def basename(path):
        """
        获取文件名：
        输入参数：path
        返回参数：basename
        说明：该方法提取路径中的文件名，path指定文件路径（支持list）；若是文件夹路径则返回文件夹名。
        """
        x = type(path)
        if x is str:
            return os.path.basename(path)
        if x is list or x is tuple:
            basename = []
            for i in path:
                basename.append(os.path.basename(i))
            return tuple(basename)
# ------------------------------------------------------------------------------
    @staticmethod
    def dirname(path):
        """
        获取文件夹名：
        输入参数：path
        返回参数：dirname
        说明：该方法提取路径中的文件夹名，path指定文件路径（支持list）；若是文件夹路径则返回上一级问价夹路径。
        """
        x = type(path)
        if x is str:
            return os.path.dirname(path)
        if x is list or x is tuple:
            dirname = []
            for i in path:
                dirname.append(os.path.dirname(i))
            return tuple(dirname)
# ------------------------------------------------------------------------------
    @staticmethod
    def scan(directory, sub=False, prefix=None, postfix=None, ret_dir=False, ret_file=True):
        """
        扫描文件：
        输入参数：directory, sub=False, prefix=None, postfix=None, ret_dir=False, ret_file=True
        返回参数：info
        说明：该方法在指定目录（directory）下进行文件扫描，
        参数sub指定是否对子目录扫描（默认不扫描），
        参数prefix、postfix分别指定文件名的前缀和后缀，
        参数ret_dir指定结果是否包含目录（默认不包含），
        参数ret_file指定结果是否包含文件（默认包含）。
        """
        info = []
        # TODO : return dir via dir tree
        for root, sub_dirs, files in os.walk(directory):
            if ret_dir == True:
                for sub_dir in sub_dirs:
                    info.append(os.path.join(root, sub_dir))
            if ret_file == True:
                for special_file in files:
                    if postfix and not special_file.endswith(postfix):
                        continue
                    if prefix and not special_file.startswith(prefix):
                        continue
                    info.append(os.path.join(root, special_file))
            if sub == False:
                sub_dirs[:] = []
        info.sort()
        return tuple(info)
# ------------------------------------------------------------------------------
    @staticmethod
    def copy(srcpath, dstpath):
        """
        拷贝文件或文件夹：
        输入参数：srcpath 源文件路径，dstpath 目的文件路径
        返回参数：True 成功，False 失败
        说明：调用该方法将文件从源路径拷贝到目的路径。
        """
        if os.path.isfile(srcpath):
            try:
                dirname = os.path.dirname(dstpath)
                if not os.path.exists(dirname):
                    os.makedirs(dirname)
                shutil.copyfile(srcpath, dstpath)
            except Exception as e:
                return False
            print("copy {} \r\n ==> {}".format(srcpath, dstpath))
            return True

        if os.path.isdir(srcpath):
            try:
                dirname = os.path.dirname(dstpath)
                if not os.path.exists(dirname):
                    os.makedirs(dirname)
                shutil.copytree(srcpath, dstpath)
            except Exception as e:
                return False
            print("copy {} \r\n ==> {}".format(srcpath, dstpath))
            return True

        return False
# ------------------------------------------------------------------------------
    @staticmethod
    def move(srcpath, dstpath):
        """
        移动文件或文件夹：
        输入参数：srcpath 源路径，dstpath 目的路径
        返回参数：True 成功，False 失败
        说明：调用该方法将文件从源路径移动到目的路径。
        """
        if os.path.isfile(srcpath) or os.path.isdir(srcpath):
            try:
                dirname = os.path.dirname(dstpath)
                if not os.path.exists(dirname):
                    os.makedirs(dirname)
                shutil.move(srcpath, dstpath)
            except Exception as e:
                return False
            print("move {} \r\n ==> {}".format(srcpath, dstpath))
            return True

        return False
# ------------------------------------------------------------------------------
    @staticmethod
    def remove(rmpath):
        """
        删除文件或文件夹：
        输入参数：rmpath 删除文件或文件夹路径
        返回参数：True 成功，False 失败
        说明：调用该方法将文件从源路径删除。
        """
        if os.path.isfile(rmpath):
            try:
                os.remove(rmpath)
            except Exception as e:
                return False
            print("removed {}".format(rmpath))
            return True

        if os.path.isdir(rmpath):
            try:
                # os.removedirs(rmpath)
                shutil.rmtree(rmpath)
            except Exception as e:
                return False
            print("removed {}".format(rmpath))
            return True

        return True
# ------------------------------------------------------------------------------
    @staticmethod
    def rename(srcpath, dstpath):
        """
        重命名文件或文件夹：
        输入参数：srcpath 源路径，dstpath 重命名路径
        返回参数：True 成功，False 失败
        说明：调用该方法将文件重命名。
        """
        if os.path.isfile(srcpath) or os.path.isdir(srcpath):
            try:
                os.rename(srcpath, dstpath)
            except Exception as e:
                return False
            return True

        return False
# ------------------------------------------------------------------------------
    @staticmethod
    def archive(srcdir, dstdir = None, buname = None, format = "zip"):
        """
        文件归档：
        输入参数：srcdir          需要归档的文件路径
                 dstdir = None   归档路径，不包括文件名，不指定时默认归档到同级文件夹下
                 buname = None   归档文件名，不包含后缀，不指定时默认使用“backup_文件夹名”作为文件名
                 format = "zip"  归档格式（zip、tar、bztar、gztar），默认使用zip
        返回参数：True 成功，False 失败
        说明：调用该方法将文件归档至指定目录下。
        """
        if not os.path.exists(srcdir):
            print("{} not exist!".format(srcdir))
            return False

        try:
            if buname == None:
                buname = "backup_" + fbasic.basename(srcdir)
            if dstdir == None:
                dstdir = fbasic.dirname(srcdir)
            if not fbasic.ensure(dstdir):
                print("{} not exist!".format(dstdir))
                return False
            dstdir = fbasic.join(dstdir, buname)
            shutil.make_archive(dstdir, format, srcdir)
        except Exception as e:
            return False

        return True
# ------------------------------------------------------------------------------
    @staticmethod
    def archive_unpack(srcpath, dstpath = None):
        """
        归档文件释放：
        输入参数：srcpath          需要释放的归档文件路径，包含文件名及后缀
                 dstpath = None   释放路径，不指定时默认释放到同级文件夹下
        返回参数：True 成功，False 失败
        说明：调用该方法将归档文件释放至指定目录下。
        """
        if not os.path.isfile(srcpath):
            print("{} not exist!".format(srcpath))
            return False

        try:
            if dstpath == None:
                dstpath = fbasic.dirname(srcpath)
            shutil.unpack_archive(srcpath, dstpath)
        except Exception as e:
            return False

        return True
# ------------------------------------------------------------------------------
    @staticmethod
    def split(srcpath, dstdir = None, maxsize = 1024 * 1024 * 1024, delete = True):
        """
        文件分片：
        输入参数：srcpath         需要分片的文件路径
                 dstdir = None   分片文件夹，不指定时默认分片到到同级文件夹下
                 maxsize = 1G    最大分片长度
                 delete = True   分片结束后是否删除源文件
        返回参数：True 成功，False 失败
        说明：调用该方法将文件分片至指定目录下。
        """
        if not os.path.isfile(srcpath):
            print("{} not exist!".format(srcpath))
            return False

        try:
            size = os.stat(srcpath).st_size
            basename = fbasic.basename(srcpath)

            if dstdir == None:
                dstdir = fbasic.dirname(srcpath)
            if not fbasic.ensure(dstdir):
                print("{} not exist!".format(dstdir))
                return False
            if fbasic.scan(dstdir, prefix = "{}.".format(basename)):
                print("exist old split files!")
                return False

            with open(srcpath, 'rb') as rf:
                seq = 0
                offset = 0
                while offset < size:
                    rlen = min(size - offset, maxsize)
                    dstname = "{}.{}".format(basename, seq)
                    dstpath = fbasic.join(dstdir, dstname)
                    with open(dstpath, 'wb') as wf:
                        date = rf.read(rlen)
                        wf.write(date)
                    offset = offset + rlen
                    seq = seq + 1

            if delete:
                fbasic.remove(srcpath)
        except Exception as e:
            return False

        return True
# ------------------------------------------------------------------------------
