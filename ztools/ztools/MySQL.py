#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
# 类 MySQL
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2019-04-14 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | Version(self, ...)  | 版本显示
# ----------------------------------------------------------------------------------------------------
import pymysql
# ----------------------------------------------------------------------------------------------------
class MySQL:
    """
    MySQL类提供了对MySQL数据库访问的访问。
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
            print("[ztools]-[MySQL]-[vesion:%s]" % self.__version)
        return self.__version
# ----------------------------------------------------------------------------------------------------
    def link(self, info):
        """
        打开数据库连接：
        输入参数：info
        返回参数：db 数据库操作对象
        说明：调用该方法将返回数据库操作对象。
        """
        db = pymysql.connect(host=info['host'], port=info['port'], user=info['user'], passwd=info['passwd'], db=info['db'], charset=info['charset'])
        return db
# ----------------------------------------------------------------------------------------------------
    def unlink(self, db):
        # 关闭数据库连接
        db.close()
# ----------------------------------------------------------------------------------------------------
    def version(self, db):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute() 方法执行 SQL 查询 
        cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        return("mysql version : " + data[0])
# ----------------------------------------------------------------------------------------------------
    def commit(self, db, sql):
        cursor = db.cursor()
        #print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            # 执行成功
            return True
        except:
            # 错误回滚
            db.rollback()
            # 执行失败
            return False
# ----------------------------------------------------------------------------------------------------
    def fetch(self, db, sql):
        cursor = db.cursor()
        #print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 获取所有记录列表
            return cursor.fetchall()
        except:
            return ()
# ----------------------------------------------------------------------------------------------------
    def update(self, db, tab, obj):
        obj2 = []
        for akey,avalue in obj.items():
            #print('%s = %s' % (akey,avalue))
            obj2.append('%s = \'%s\'' % (akey, avalue))
        obj2 = [', '.join(obj2[1:]), obj2[0]]
        #print(obj2)
        # SQL 插入语句
        sql = "UPDATE %s SET %s WHERE %s" % (tab, obj2[0], obj2[1])
        if commit(db, sql):
            return True
        else:
            return False
# ----------------------------------------------------------------------------------------------------
    def insert(self, db, tab, obj):
        key = []
        val = []
        for akey,avalue in obj.items():
            #print(akey, avalue)
            key.append(akey)
            val.append(avalue)
        key = ', '.join(key)
        val = str(val)[1:-1]
        obj2 = [key, val]
        #print(obj2)
        # SQL 插入语句
        sql = "INSERT INTO %s(%s) VALUES(%s)" % (tab, obj2[0], obj2[1])
        # cmd(db, sql)
        if commit(db, sql):
            return True
        else:
            return update(db, tab, obj)
# ----------------------------------------------------------------------------------------------------
    def select(self, db, tab, where=None):
        sql = "select * from %s" % tab
        if where != None:
            sql = "%s where %s" % (sql, where)
        #print(sql)
        return fetch(db, sql)
# ----------------------------------------------------------------------------------------------------
