import sys
sys.path.append(r'..\..\ztools\ztools')
import File


fil = File.File()
fil.Version(isShow = True)
fil.copy(r'.\ts_File\ts.txt', r'.\ts_File\folder1\test1.txt')
input("按回车（Enter）继续")
fil.copy(r'.\ts_File\ts.txt', r'.\ts_File\folder2\test2.txt')
input("按回车（Enter）继续")
fil.copy(r'.\ts_File\ts.txt', r'.\ts_File\test.txt')
input("按回车（Enter）继续")
fil.move(r'.\ts_File\test.txt', r'.\ts_File\testx.txt')
input("按回车（Enter）继续")
fil.delete(r'.\ts_File\testx.txt')
input("按回车（Enter）继续")
