import sys
sys.path.append('..\\ztools\\ztools')
from common.file import fbasic

fbasic.archive('.\\ts_fbasic\\folder1')
input("按回车（Enter）继续")
fbasic.archive('.\\ts_fbasic\\folder1', '.\\ts_fbasic\\backup')
input("按回车（Enter）继续")
fbasic.archive('.\\ts_fbasic\\folder1', '.\\ts_fbasic', "backup1")
input("按回车（Enter）继续")
fbasic.archive('.\\ts_fbasic\\folder1', '.\\ts_fbasic', "backup1", "tar")
input("按回车（Enter）继续")
fbasic.archive_unpack('.\\ts_fbasic\\backup\\backup_folder1.zip')
input("按回车（Enter）继续")
fbasic.archive_unpack('.\\ts_fbasic\\backup1.tar', '.\\ts_fbasic\\backup_folder1')
input("按回车（Enter）继续")
