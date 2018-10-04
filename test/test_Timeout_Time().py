import ztools
import time

ztools_timeout = ztools.Timeout()
ztools_timeout.Version(isShow = True)

print("开始：%0.3f秒" % ztools_timeout.Time())
time.sleep(0.1)
print("计时1时间：%0.3f秒" % ztools_timeout.Time())
time.sleep(1.0)
print("计时2时间：%0.3f秒" % ztools_timeout.Time())
time.sleep(10)
print("计时3时间：%0.3f秒" % ztools_timeout.Time())

input()