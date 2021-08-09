import sys
sys.path.insert(0, r'..\ztools')
from ztools.gui.plot import plot
from ztools.common.file import fbasic
from ztools.utils.timeout import timeout

# 参考：
# https://matplotlib.org/api/pyplot_summary.html

fb = fbasic()
fb.ensure('.\\ts_plot')

plt = plot()
plt.figure('测试Plot（scatter）')
plt.title('测试Plot')
# sub 1
plt.subplot(121)
plt.title('plot')
plt.label(xlabel='time', ylabel='value')
points = []
points.append(plt.point(1, 10))
points.append(plt.point(2, 20))
points.append(plt.point(3, 30))
points.append(plt.point(4, 40))
points.append(plt.point(5, 50))
plt.plot(points, label = "plot")
plt.legend()
# sub 2
plt.subplot(122)
plt.title('xyplot')
plt.label(xlabel='x轴', ylabel='y轴')
x  = [1, 2, 3, 4, 5]
y1 = [1, 2, 3, 4, 5]
y2 = [5, 4, 3, 2, 1]
y3 = [2, 3, 4, 3, 2]
y4 = [4, 3, 2, 3, 4]
plt.xyplot(x, y1, label = "xyplot1", color = 'red')
plt.xyplot(x, y2, label = "xyplot2", linewidth = 1.0)
plt.xyplot(x, y3, label = "xyplot3", linestyle = '--')
plt.xyplot(x, y4, label = "xyplot4", linestyle = '-.')
plt.xyplot([3, 3], [1, 2], label = "xyplot", linewidth = 2.0)
plt.xyplot([3, 3], [4, 5], label = "xyplot", linewidth = 2.0)
plt.legend()
plt.savefig('.\\ts_plot\\ts_plot_plot.png')
plt.close()

timeout = timeout()
plt.figure('测试imread和imshow方法')
print("开始： %0.3f sec" % timeout.time())
image = plt.imread('.\\ts_Plot\\ts_plot_plot.png')
print("用时： %0.3f sec" % timeout.time())
plt.imshow(image)
plt.close()

input("按回车（Enter）继续")
