import ztools
import time

ztools_timeout = ztools.Timeout()
ztools_timeout.Version(isShow = True)

print(ztools_timeout.Time())
time.sleep(0.1)
print(ztools_timeout.Time())
time.sleep(1.0)
print(ztools_timeout.Time())
time.sleep(10)
print(ztools_timeout.Time())

input()