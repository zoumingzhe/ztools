import sys
sys.path.insert(0, r'..\ztools')
from ztools.tool.tprint import tprint
from ztools.tool.tprint import AnsiStyle as style
from ztools.tool.tprint import AnsiFore as fore
from ztools.tool.tprint import AnsiBack as back

print("-----")
print(tprint)
tprint.std("123")

print("-----")
tp = tprint()
print(tp)
tp.std("123")

input("按回车（Enter）继续")
