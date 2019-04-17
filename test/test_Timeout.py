import ztools
import time

ztools_timeout = ztools.Timeout()
ztools_timeout.Version(isShow = True)

print("开始计时： %0.3f sec" % ztools_timeout.Time())
time.sleep(0.1)
print("延时 0.1 sec： %0.3f sec" % ztools_timeout.Time())
print("TimeStart值： %0.3f sec" % ztools_timeout.GetTimeStart())

print("重置计时： %0.3f sec" % ztools_timeout.Reset())
time.sleep(1)
print("延时 1 sec： %0.3f sec" % ztools_timeout.Time())
print("TimeStart值： %0.3f sec" % ztools_timeout.GetTimeStart())

print("重置计时： %0.3f sec" % ztools_timeout.Reset())
print("超时判断（3 sec）：")
for n in range(5):
    time.sleep(1)
    if ztools_timeout.Timeout(3):
        print("计时 %d 时间： %0.3f sec，超时判断：True" % (n, ztools_timeout.Time()))
    else:
        print("计时 %d 时间： %0.3f sec，超时判断：False" % (n, ztools_timeout.Time()))
print("TimeStart值：%0.3f sec" % ztools_timeout.GetTimeStart())

print("重置计时： %0.3f sec" % ztools_timeout.Reset())
print("超时判断（3 sec）：")
for n in range(10):
    time.sleep(1)
    if ztools_timeout.Timeout(3):
        print("计时 %d 时间： %0.3f sec，超时判断：True" % (n, ztools_timeout.Time()))
    else:
        print("计时 %d 时间： %0.3f sec，超时判断：False" % (n, ztools_timeout.Time()))
print("TimeStart值： %0.3f sec" % ztools_timeout.GetTimeStart())

input()
