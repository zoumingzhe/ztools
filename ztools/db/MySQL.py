# coding=utf-8
# ------------------------------------------------------------------------------
# 类 MySQL
# ------------------------------------------------------------------------------
# 变更履历：
# 2019-04-14 | Zou Mingzhe   | Ver0.1  | 初始版本
# ------------------------------------------------------------------------------
# MAP：
# 已测试 | Version(self, ...)           | 版本显示
# 未测试 | link(self, ...)              | 
# 未测试 | unlink(self)                 | 
# 未测试 | version(self)                | 
# ------------------------------------------------------------------------------
from .CRUD import CRUD
import pymysql
# ------------------------------------------------------------------------------
class MySQL(CRUD):
    """
    MySQL类提供了对MySQL数据库访问的封装，它是基于pymysql实现的。
    """
    def __init__(self):
        self.__version = "0.1"
        self.db = None
    def __del__(self):
        if self.db != None:
            self.db.close()
# ------------------------------------------------------------------------------
    def Version(self, isShow = False):
        """
        版本显示：
        输入参数：isShow = False
        返回参数：self.__version
        说明：调用该方法将返回类的版本号，若isShow == True则会在屏幕上打印版本号。
        """
        if(isShow):
            print("[ztools]-[MySQL]-[vesion:%s]" % self.__version)
        return self.__version
# ------------------------------------------------------------------------------
    def link(self, info):
        """
        打开数据库连接：
        输入参数：info
        返回参数：self.__db 数据库操作对象
        说明：调用该方法将返回数据库操作对象。
        """
        self.db = pymysql.connect(host=info['host'], port=info['port'], user=info['user'], passwd=info['passwd'], db=info['db'], charset=info['charset'])
        return self.db
# ------------------------------------------------------------------------------
    def unlink(self):
        """
        关闭数据库连接：
        输入参数：
        返回参数：
        说明：调用该方法将释放数据库操作对象。
        """
        self.db.close()
        self.db = None
        return self.db
# ------------------------------------------------------------------------------
    def version(self):
        """
        MySQL版本显示：
        输入参数：
        返回参数：
        说明：调用该方法将返回所连接的MySQL版本号。
        """
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.db.cursor()
        # 使用 execute() 方法执行 SQL 查询 
        cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        # 关闭游标
        cursor.close()
        return("mysql version : " + data[0])
# ------------------------------------------------------------------------------
