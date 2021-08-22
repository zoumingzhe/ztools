import sys
sys.path.append(r'..\..\ztools\ztools')
import File


fil = File.File()
fil.Version(isShow = True)
input("按回车（Enter）继续")
res = fil.get_path(r'.\ts_File', ["test1", "test2"])
print(res)
print(fil.get_folder(res))
print(fil.get_name(res))
input("按回车（Enter）继续")
res = fil.get_path(r'.\ts_File', "test")
print(res)
print(fil.get_folder(res))
print(fil.get_name(res))
input("按回车（Enter）继续")
