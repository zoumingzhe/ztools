import sys
sys.path.append(r'..\ztools\ztools')
import File


fil = File.File()
fil.Version(isShow = True)
input("按回车（Enter）扫描.\\ts_File文件夹下文件")
res = fil.scan(r'.\ts_File')
print(res)
input("按回车（Enter）扫描.\\ts_File文件夹及其子文件夹下文件")
res = fil.scan(r'.\ts_File', sub=True)
print(res)
input("按回车（Enter）扫描.\\ts_File文件夹及其子文件夹下sub开头文件")
res = fil.scan(r'.\ts_File', sub=True, prefix="sub")
print(res)
input("按回车（Enter）扫描.\\ts_File文件夹及其子文件夹下.file文件")
res = fil.scan(r'.\ts_File', sub=True, postfix=".file")
print(res)
input("按回车（Enter）扫描.\\ts_File2文件夹下文件")
res = fil.scan(r'.\ts_File2')
print(res)
input("按回车（Enter）继续")
