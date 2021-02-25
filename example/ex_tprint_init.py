from ztools import tprint
from ztools import AnsiStyle as style
from ztools import AnsiFore as fore
from ztools import AnsiBack as back

print("-----")
print(tprint)
tprint.std("123")

print("-----")
tp = tprint()
print(tp)
tp.std("123")

input("按回车（Enter）继续")
