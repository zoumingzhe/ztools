import sys
sys.path.insert(0, r'..\ztools')
from ztools.tool.tprint import tprint

tp = tprint()
tp.color("123", style = 4, foreground = 31, background = 47)
tp.flush()
tp.color("123", style = 4, foreground = 31)
tp.flush()
tp.color("123", style = 4, background = 47)
tp.flush()
tp.color("123", style = 4)
tp.flush()
tp.color("123")
tp.flush()

print("-----")

tp.color("123", foreground = 31, background = 47)
tp.flush()
tp.color("123", foreground = 31)
tp.flush()
tp.color("123", background = 47)
tp.flush()
tp.color("123")
tp.flush()

input("按回车（Enter）继续")
