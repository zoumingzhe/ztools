import sys
sys.path.append(r'..\..\ztools\ztools')
import File


fil = File.File()
fil.Version(isShow = True)
path = '.\\ts_File\\ensure'

print(path)
print(fil.ensure(path, isCreate = False))
input("按回车（Enter）继续")

print(path)
print(fil.ensure(path, isCreate = True))
input("按回车（Enter）继续")

print(path)
print(fil.ensure(path, isCreate = False))
input("按回车（Enter）继续")
