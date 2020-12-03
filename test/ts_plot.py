import sys
sys.path.append(r'..\ztools\ztools')
from file.filebase import filebase
from GUI.plot import plot
from tool.timeout import timeout

# 参考：
# https://blog.csdn.net/weixin_40040404/article/details/81185564

fb = filebase()
fb.ensure('.\\ts_plot')

plt = plot('测试Plot（scatter）')
plt.Version(isShow = True)
plt.label(xlabel='x轴', ylabel='y轴')
points = []
points.append(plt.point('星期一', '13:00', 10))
points.append(plt.point('星期二', '14:30', 20))
points.append(plt.point('星期三', '15:00', 30))
points.append(plt.point('星期四', '16:00', 40))
plt.scatter(points)
plt.save('.\\ts_plot\\ts_plot_scatter.png')
plt.show()

plt = plot('测试Plot（xyscatter）')
plt.Version(isShow = True)
plt.label(xlabel='x轴', ylabel='y轴')
x = [1, 1, 2, 2]
y = [1, 2, 1, 2]
plt.xyscatter(x, y)
plt.save('.\\ts_plot\\ts_plot_xyscatter.png')
plt.show()

timeout = timeout()
timeout.Version(isShow = True)
print("开始： %0.3f sec" % timeout.Time())
plt_image = plot('测试read和showimage方法')
image = plt_image.read('.\\ts_Plot\\ts_plot_scatter.png')
print("用时： %0.3f sec" % timeout.Time())
plt_image.showimage(image)

input("按回车（Enter）继续")
