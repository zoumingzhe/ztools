import sys
sys.path.append(r'../../ztools')
from data.fbasic import fbasic


print("扫描.\\ts_fbasic目录下文件")
for i in fbasic.scan(r'.\ts_fbasic'):
    print(i)

print("扫描.\\ts_fbasic目录及其子目录下文件")
for i in fbasic.scan(r'.\ts_fbasic', sub=True):
    print(i)

print("扫描.\\ts_fbasic目录及其子目录下sub开头文件")
for i in fbasic.scan(r'.\ts_fbasic', sub=True, prefix="sub"):
    print(i)

print("扫描.\\ts_fbasic目录及其子目录下.file文件")
for i in fbasic.scan(r'.\ts_fbasic', sub=True, postfix=".file"):
    print(i)

print("扫描.\\ts_fbasic2目录下文件")
for i in fbasic.scan(r'.\ts_fbasic2'):
    print(i)

input("按回车（Enter）继续")
