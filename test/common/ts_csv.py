import sys
sys.path.append(r'..\..\ztools\ztools')
from common.xls import csv

sheet = csv.read(r'.\ts_csv\input1.csv', cleanblank = True)
csv.write(r'.\ts_csv\input1.out', sheet)
sheet = csv.read(r'.\ts_csv\input2.csv', cleanblank = False)
csv.write(r'.\ts_csv\input2.out', sheet)

input("按回车（Enter）继续")
