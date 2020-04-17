import sys
sys.path.append(r'..\ztools\ztools')
from tool.timeout import timeout
import time

timeout = timeout()
timeout.Version(isShow = True)

print("开始计时： %0.3f sec" % timeout.Time())
time.sleep(0.1)
print("延时 0.1 sec： %0.3f sec" % timeout.Time())
print("TimeStart值： %0.3f sec" % timeout.GetTimeStart())

print("重置计时： %0.3f sec" % timeout.Reset())
time.sleep(1)
print("延时 1 sec： %0.3f sec" % timeout.Time())
print("TimeStart值： %0.3f sec" % timeout.GetTimeStart())

print("重置计时： %0.3f sec" % timeout.Reset())
print("超时判断（3 sec）：")
for n in range(5):
    time.sleep(1)
    if timeout.Timeout(3):
        print("计时 %d 时间： %0.3f sec，超时判断：True" % (n, timeout.Time()))
    else:
        print("计时 %d 时间： %0.3f sec，超时判断：False" % (n, timeout.Time()))
print("TimeStart值：%0.3f sec" % timeout.GetTimeStart())

print("重置计时： %0.3f sec" % timeout.Reset())
print("超时判断（5 sec）：")
for n in range(10):
    time.sleep(1)
    if timeout.Timeout(5):
        print("计时 %d 时间： %0.3f sec，超时判断：True" % (n, timeout.Time()))
    else:
        print("计时 %d 时间： %0.3f sec，超时判断：False" % (n, timeout.Time()))
print("TimeStart值： %0.3f sec" % timeout.GetTimeStart())

input("按回车（Enter）继续")
