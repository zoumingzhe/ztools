import sys
sys.path.append(r'..\ztools\ztools')
from GUI.plot import plot
from tool.timeout import timeout

# 参考：
# https://blog.csdn.net/weixin_40040404/article/details/81185564


plt = plot('测试Plot')
plt.Version(isShow = True)
plt.label(xlabel='x轴')
# point = plt.point(0, 0, 50)
# #print(point)
# plt.Scatter(point)
# points = [plt.point(1, 1, 10), plt.point(1, 2, 20), plt.point(2, 1, 30), plt.point(2, 2, 40)]
# #print(points)
# plt.Scatter(points)
points = []
points.append(plt.point('星期一', '13:00', 10))
points.append(plt.point('星期二', '14:30', 20))
points.append(plt.point('星期三', '15:00', 30))
points.append(plt.point('星期四', '16:00', 40))
plt.scatter(points)
#plt.scatter(1, 1)
#plt.scatter(1, 2)
#plt.scatter(2, 1)
#plt.scatter(2, 2)
#plt.grid()
plt.save('.\\ts_plot\\ts_plot.png')
plt.show()



ztools_timeout = Timeout.Timeout()
ztools_timeout.Version(isShow = True)
plt_image = ztools.Plot(title = None)
print("开始： %0.3f sec" % ztools_timeout.Time())
#plt_image = Plot('测试Read和Image方法')
image = plt_image.Read('.\\ts_Plot\\ts_Plot.png')
plt_image.ShowImage(image)
print("用时： %0.3f sec" % ztools_timeout.Time())

input("按回车（Enter）继续")
