import sys
sys.path.append(r'../../ztools')
from data.fbasic import fbasic


print("扫描.\\ts_fbasic目录下目录")
for i in fbasic.scan(r'.\ts_fbasic', ret_dir = True, ret_file = False):
    print(i)

print("扫描.\\ts_fbasic目录及其子目录下目录")
for i in fbasic.scan(r'.\ts_fbasic', sub=True, ret_dir = True, ret_file = False):
    print(i)

print("扫描.\\ts_fbasic2目录下目录")
for i in fbasic.scan(r'.\ts_fbasic2', sub=True, ret_dir = True, ret_file = False):
    print(i)

input("按回车（Enter）继续")
