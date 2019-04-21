import sys
sys.path.append(r'..\ztools\ztools')
import Plot
import Timeout

# 参考：
# https://blog.csdn.net/weixin_40040404/article/details/81185564


plt = Plot.Plot('测试Plot')
plt.Version(isShow = True)
plt.Label(xlabel='x轴')
# point = plt.Point(0, 0, 50)
# #print(point)
# plt.Scatter(point)
# points = [plt.Point(1, 1, 10), plt.Point(1, 2, 20), plt.Point(2, 1, 30), plt.Point(2, 2, 40)]
# #print(points)
# plt.Scatter(points)
points = [plt.Point('星期一', '13:00', 10), plt.Point('星期二', '14:30', 20), plt.Point('星期三', '15:00', 30), plt.Point('星期四', '16:00', 40)]
plt.Scatter(points)
#plt.Scatter(1, 1)
#plt.Scatter(1, 2)
#plt.Scatter(2, 1)
#plt.Scatter(2, 2)
#plt.Grid()
plt.Save('.\\ts_Plot\\ts_Plot.png')
plt.Show()



ztools_timeout = Timeout.Timeout()
ztools_timeout.Version(isShow = True)
plt_image = ztools.Plot(title = None)
print("开始： %0.3f sec" % ztools_timeout.Time())
#plt_image = Plot('测试Read和Image方法')
image = plt_image.Read('.\\ts_Plot\\ts_Plot.png')
plt_image.ShowImage(image)
print("用时： %0.3f sec" % ztools_timeout.Time())

input("按回车（Enter）继续")
