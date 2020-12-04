import sys
sys.path.append(r'..\ztools\ztools')
from data.filebase import filebase
from data.hash import hash

hash = hash()

print(hash.md5("This a md5 test!".encode("utf-8")))
data = "This a md5 test!".encode("utf-8")
print(hash.md5(data))

print(hash.sha1("This a md5 test!".encode("utf-8")))
data = "This a md5 test!".encode("utf-8")
print(hash.sha1(data))

input("按回车（Enter）继续")
