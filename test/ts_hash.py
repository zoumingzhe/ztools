import sys
sys.path.append(r'..\ztools\ztools')
from data.filebase import filebase
from data.hash import hash

hash = hash()

print('**********md5**********')
print(hash.md5())
print(hash.md5(filename = ".\\ts_hash\\ts_hash_md5.txt".encode("utf-8")))
print(hash.md5(filename = [".\\ts_hash\\ts_hash_md5.txt", None]))
print(hash.md5(filename = (".\\ts_hash\\ts_hash_md5.txt", None)))
print(hash.md5(filename = [".\\ts_hash\\ts_hash_md5.txt"]))
print(hash.md5(filename = (".\\ts_hash\\ts_hash_md5.txt")))
print(hash.md5(filename = ".\\ts_hash\\ts_hash_md5.txt"))
print(hash.md5("This a md5 test!".encode("utf-8")))
data = "This a md5 test!".encode("utf-8")
print(hash.md5(data))
print(data)
data = "This a md5 test!"
print(hash.md5(data, encoding = "utf-8"))
print(data)
obj = hash.md5()
obj.update(data.encode("utf-8"))
print(obj.hexdigest())

print('**********sha1**********')
print(hash.sha1())
print(hash.sha1(filename = ".\\ts_hash\\ts_hash_sha1.txt".encode("utf-8")))
print(hash.sha1(filename = [".\\ts_hash\\ts_hash_sha1.txt", None]))
print(hash.sha1(filename = (".\\ts_hash\\ts_hash_sha1.txt", None)))
print(hash.sha1(filename = [".\\ts_hash\\ts_hash_sha1.txt"]))
print(hash.sha1(filename = (".\\ts_hash\\ts_hash_sha1.txt")))
print(hash.sha1(filename = ".\\ts_hash\\ts_hash_sha1.txt"))
print(hash.sha1("This a sha1 test!".encode("utf-8")))
data = "This a sha1 test!".encode("utf-8")
print(hash.sha1(data))
print(data)
data = "This a sha1 test!"
print(hash.sha1(data, encoding = "utf-8"))
print(data)
obj = hash.sha1()
obj.update(data.encode("utf-8"))
print(obj.hexdigest())

input("按回车（Enter）继续")
