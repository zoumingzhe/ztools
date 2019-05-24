import sys
sys.path.append('..\\ztools\\ztools')
import File


fil = File.File()
fil.Version(isShow = True)
input("按回车（Enter）继续")
fil.archive('.\\ts_File\\folder1')
input("按回车（Enter）继续")
fil.archive('.\\ts_File\\folder1', '.\\ts_File\\backup')
input("按回车（Enter）继续")
fil.archive('.\\ts_File\\folder1', '.\\ts_File', "backup1")
input("按回车（Enter）继续")
fil.archive('.\\ts_File\\folder1', '.\\ts_File', "backup1", "tar")
input("按回车（Enter）继续")
fil.archive_unpack('.\\ts_File\\backup\\backup_folder1.zip')
input("按回车（Enter）继续")
fil.archive_unpack('.\\ts_File\\backup1.tar', '.\\ts_File\\backup_folder1')
input("按回车（Enter）继续")
