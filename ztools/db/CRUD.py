# coding=utf-8
# ------------------------------------------------------------------------------
# 类 CRUD
# ------------------------------------------------------------------------------
# 变更履历：
# 2020-09-21 | Zou Mingzhe   | Ver0.1  | 初始版本
# ------------------------------------------------------------------------------
# MAP：
# 未测试 | execute(self, ...)           | 
# 未测试 | fetch(self, ...)             | 
# 未测试 | insert(self, ...)            | 
# 未测试 | select(self, ...)            | 
# 未测试 | update(self, ...)            | 
# 未测试 | delete(self, ...)            | 
# ------------------------------------------------------------------------------
from abc import ABCMeta, abstractmethod
# ------------------------------------------------------------------------------
class CRUD:
    """
    SQLite类提供了对SQLite数据库访问的封装，它是基于sqlite3实现的。
    """
    __metaclass__ = ABCMeta
    def __init__(self):
        pass
    def __del__(self):
        pass
# ------------------------------------------------------------------------------
    @abstractmethod
    def link(self, db):
        """
        打开数据库连接：
        输入参数：db
        返回参数：self.__db 数据库操作对象
        说明：调用该方法将返回数据库操作对象。
        """
        pass
# ------------------------------------------------------------------------------
    @abstractmethod
    def unlink(self):
        """
        关闭数据库连接：
        输入参数：
        返回参数：
        说明：调用该方法将释放数据库操作对象。
        """
        pass
# ------------------------------------------------------------------------------
    def execute(self, sql):
        """
        提交：
        输入参数：sql 执行语句
        返回参数：成功/失败
        说明：调用该方法将执行sql语句并提交。
        """
        db = getattr(self, 'db')
        if db == None:
            return False
        cursor = db.cursor()
        #print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            cursor.close()
            db.commit()
            # 执行成功
            return True
        except:
            cursor.close()
            # 错误回滚
            db.rollback()
            # 执行失败
            return False
# ------------------------------------------------------------------------------
    def fetch(self, sql):
        """
        检索：
        输入参数：sql 检索条件
        返回参数：检索信息
        说明：调用该方法将返回检索到的信息。
        """
        db = getattr(self, 'db')
        if db == None:
            return False
        cursor = db.cursor()
        #print(sql)
        try:
            ret = []
            # 执行sql语句
            cursor.execute(sql)
            # 获取所有记录列表
            for row in cursor:
                ret.append(row)
            cursor.close()
            return tuple(ret)
        except:
            cursor.close()
            return ()
# ------------------------------------------------------------------------------
    def insert(self, tab, obj):
        """
        插入：
        输入参数：tab 表，obj 插入数据{'key':value}
        返回参数：成功/失败
        说明：调用该方法将向指定表插入数据。
        """
        keys = []
        vals = []
        for akey,avalue in obj.items():
            #print(akey, avalue)
            keys.append(akey)
            vals.append(avalue)
        keys = ', '.join(keys)
        vals = str(vals)[1:-1]
        sql = "INSERT INTO %s(%s) VALUES(%s)" % (tab, keys, vals)
        #print(sql)
        return self.execute(sql)
# ------------------------------------------------------------------------------
    def select(self, tab, where=None):
        """
        插入：
        输入参数：tab 表
        返回参数：元组
        说明：调用该方法将返回指定表数据。
        """
        sql = "SELECT * FROM %s" % tab
        if where != None:
            sql = "%s WHERE %s" % (sql, where)
        #print(sql)
        return self.fetch(sql)
# ------------------------------------------------------------------------------
    def update(self, tab, obj, where):
        """
        插入：
        输入参数：tab 表，obj 更新数据{'key':value}，where 更新条件
        返回参数：成功/失败
        说明：调用该方法将更新指定表数据。
        """
        cols = []
        for akey,avalue in obj.items():
            #print(akey, avalue)
            if type(avalue) != str:
                #print("%s = %s" % (akey, str(avalue)))
                cols.append("%s = %s" % (akey, str(avalue)))
            else:
                #print("%s = '%s'" % (akey, str(avalue)))
                cols.append("%s = '%s'" % (akey, str(avalue)))
        cols = ', '.join(cols)
        sql = "UPDATE %s SET %s WHERE %s" % (tab, cols, where)
        #print(sql)
        return self.execute(sql)
# ------------------------------------------------------------------------------
    def delete(self, tab, where=None):
        """
        删除：
        输入参数：tab 表
        返回参数：成功/失败
        说明：调用该方法将从指定表删除数据。
        """
        sql = "DELETE FROM %s" % tab
        if where != None:
            sql = "%s where %s" % (sql, where)
        #print(sql)
        return self.execute(sql)
# ------------------------------------------------------------------------------
