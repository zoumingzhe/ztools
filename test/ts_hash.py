import sys
sys.path.append(r'..\ztools\ztools')
from data.filebase import filebase
from data.hash import hash

hash = hash()

print(hash.md5(filename = ".\\ts_hash\\ts_hash_md5.txt"))
print(hash.md5("This a md5 test!".encode("utf-8")))
data = "This a md5 test!".encode("utf-8")
print(hash.md5(data))
print(data)
data = "This a md5 test!"
print(hash.md5(data, encoding = "utf-8"))
print(data)
print(hash.md5())
print(data)

print(hash.sha1(filename = ".\\ts_hash\\ts_hash_sha1.txt"))
print(hash.sha1("This a sha1 test!".encode("utf-8")))
data = "This a sha1 test!".encode("utf-8")
print(hash.sha1(data))
print(data)
data = "This a sha1 test!"
print(hash.sha1(data, encoding = "utf-8"))
print(data)
print(hash.sha1())
print(data)

input("按回车（Enter）继续")
