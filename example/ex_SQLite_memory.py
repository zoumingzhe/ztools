from ztools import SQLite

db = SQLite()
db.link(":memory:")
print(db.execute('''CREATE TABLE test
      (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);'''))
print(db.insert("test", {'ID':1,'NAME':'name1','AGE':28}))
print(db.insert("test", {'ID':2,'NAME':'name2','AGE':28}))
print(db.execute("INSERT INTO test(ID, NAME, AGE) VALUES(3, 'name3', 29)"))
print(db.execute("INSERT INTO test(ID, NAME, AGE) VALUES(4, 'name4', 30)"))
print(db.select("test"))
print(db.update("test", {'NAME':'name0', 'AGE':29}, "NAME = 'name1'"))
print(db.update("test", {'AGE':27}, 'AGE = 28'))
print(db.select("test"))
print(db.delete("test", "NAME = 'name2'"))
print(db.select("test"))
db.unlink()
