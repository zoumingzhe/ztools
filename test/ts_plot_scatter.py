import sys
sys.path.insert(0, r'..\ztools')
from ztools.gui.plot import plot
from ztools.common.file import fbasic
from ztools.tool.timeout import timeout

# 参考：
# https://matplotlib.org/api/pyplot_summary.html

fb = fbasic()
fb.ensure('.\\ts_plot')

plt = plot()
plt.figure('测试Plot（scatter）')
plt.title('测试Plot')
plt.subplot(121)
plt.title('scatter')
plt.label(xlabel='日期', ylabel='时间')
points = []
points.append(plt.point('星期一', '13:00', 10))
points.append(plt.point('星期二', '14:30', 20))
points.append(plt.point('星期三', '15:00', 30))
points.append(plt.point('星期四', '16:00', 40))
plt.scatter(points)
plt.subplot(122)
plt.title('xyscatter')
plt.label(xlabel='x轴', ylabel='y轴')
x = [1, 1, 2, 2]
y = [1, 2, 1, 2]
plt.xyscatter(x, y)
plt.savefig('.\\ts_plot\\ts_plot_scatter.png')
plt.close()

timeout = timeout()
plt.figure('测试imread和imshow方法')
print("开始： %0.3f sec" % timeout.time())
image = plt.imread('.\\ts_Plot\\ts_plot_scatter.png')
print("用时： %0.3f sec" % timeout.time())
plt.imshow(image)
plt.close()

input("按回车（Enter）继续")
