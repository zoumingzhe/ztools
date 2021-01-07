import sys
sys.path.insert(0, r'..\ztools')
from ztools.tool.tprint import tprint
from ztools.tool.tprint import AnsiStyle as style
from ztools.tool.tprint import AnsiFore as fore
from ztools.tool.tprint import AnsiBack as back

tp = tprint()

print("-----")
tp.color("123", style.underline, fore.red, back.white)
tp.flush()
tp.color("123", style.underline, fore.red)
tp.flush()
tp.color("123", style.underline, back.white)
tp.flush()
tp.color("123", style.underline)
tp.flush()
tp.color("123")
tp.flush()

print("-----")
tp.color("123", fore.red, back.white)
tp.flush()
tp.color("123", fore.red)
tp.flush()
tp.color("123", back.white)
tp.flush()
tp.color("123")
tp.flush()

print("-----")
tp.color(123, fore.red, back.white)
tp.flush()
tp.color(123, fore.red)
tp.flush()
tp.color(123, back.white)
tp.flush()
tp.color(123)
tp.flush()

input("按回车（Enter）继续")
