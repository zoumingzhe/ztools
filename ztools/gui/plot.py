# coding=utf-8
# ------------------------------------------------------------------------------
# 类 plot
# ------------------------------------------------------------------------------
# 变更履历：
# 2022-08-08 | Zou Mingzhe   | Ver0.10 | 1.部分接口增加 @staticmethod
# 2021-08-07 | Zou Mingzhe   | Ver0.9  | 1.删除 Version(self, isShow = False)
#            |               |         | 2.增加 legend(self, *args, **kwargs)
#            |               |         | 3.修改 xyplot(self, x, y, *args, **kwargs)
#            |               |         | 4.修改 plot(self, points, *args, **kwargs)
# 2020-12-xx | Zou Mingzhe   | Ver0.8  | 1.增加 subplot(self, subtitle)
#            |               |         | 2.增加 subplots(self)
#            |               |         | 3.增加 xyscatter(self, x, y, size = None, color = None, marker = None)
#            |               |         | 4.增加 xyplot(self, x, y, color = None, linewidth = None, label = None)
#            |               |         | 5.增加 xybar(self, x, y, color = None, align = None)
#            |               |         | 6.增加 pie(self, )
# 2020-12-02 | Zou Mingzhe   | Ver0.7  | 1.优化 scatter(self, points)，多点绘制性能
#            |               |         | 2.增加 points(self, x, y, size = None, color = None, marker = None)
# 2019-04-20 | Zou Mingzhe   | Ver0.6  | 1.修改 scatter(self, points)，输入的points类型支持list或者tuple
# 2019-04-15 | Zou Mingzhe   | Ver0.5  | 1.完善帮助信息
# 2019-02-11 | Zou Mingzhe   | Ver0.4  | 1.增加 savefig(self, path)
#            |               |         | 2.增加 imread(self, path)
#            |               |         | 3.增加 showimage(self, image)
# 2019-01-28 | Zou Mingzhe   | Ver0.3  | 1.增加 grid(self)
#            |               |         | 2.增加 point(self, x, y, size = None, color = None, marker = None)
#            |               |         | 3.修改 scatter(self, points)
# 2018-11-21 | Zou Mingzhe   | Ver0.2  | 1.增加 show(self)
#            |               |         | 2.增加 label(self, xlabel = None, ylabel = None)
#            |               |         | 3.增加 scatter(self, x, y)
# 2018-11-19 | Zou Mingzhe   | Ver0.1  | 初始版本
# ------------------------------------------------------------------------------
# MAP：
# 已测试 | Version(self, ...)           | 版本显示（删除）
# 已测试 | figure(self)                 | 创建对象
# 已测试 | close(self)                  | 关闭对象
# 已测试 | show(self)                   | 显示绘图
# 已测试 | savefig(self, ...)           | 保存绘图
# 已测试 | imread(self, ...)            | 读取图像文件
# 已测试 | imshow(self, ...)            | 显示图像
# 已测试 | label(self, ...)             | 添加坐标轴标签
# 已测试 | title(self, ...)             | 添加标题
# 已测试 | grid(self)                   | 绘制网格线
# 已测试 | legend(self, ...)            | 绘制图例
# 未测试 | subplot(self)                | 绘制子图
# 未测试 | subplots(self)               | 绘制子图
# 已测试 | point(self, ...)             | 获取一个点对象
# 已测试 | points(self, ...)            | 获取多个点对象
# 已测试 | pie(self, ...)               | 绘制饼图
# 已测试 | xybar(self, ...)             | 绘制条形图
# 已测试 | xyplot(self, ...)            | 绘制折线图
# 已测试 | xyscatter(self, ...)         | 绘制散点图
# 已测试 | scatter(self, ...)           | 绘制散点图
# ------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import matplotlib.image  as img
from ..common.file import fbasic
# ------------------------------------------------------------------------------
class plot(fbasic):
    """
    plot类提供了绘图功能，它是基于matplotlib的，同时也是matplotlib的增强。
    只需要几行代码即可获得绘制图形，大大缩减了绘图的代码行数，获得高质量的编程体验。
    特性：
    1、对matplotlib功能进行整合，简单易用；
    2、支持中文，直接支持标题、坐标轴、图例等的中文显示；
    3、使用Scatter绘制散点图时，使用“点对象”作为参数，而不需要多个“向量”参数，并通过Point进一步简化了点的创建。
    参考：
    1、https://matplotlib.org/stable/api/pyplot_summary.html
    """
    def __init__(self):
        self.__version = "0.10"
        self.__figure  = None
        plt.rcParams['font.sans-serif']=['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False    # 用来正常显示负号
        # 有中文出现的情况，需要u'内容'
# ------------------------------------------------------------------------------
    def figure(self, id, figsize = None, dpi = None, facecolor = None, edgecolor = None,\
        frameon = True, clear = False):
        """
        创建对象：
        输入参数：
        返回参数：
        说明：调用该方法将创建绘图对象。
        参考：https://matplotlib.org/3.3.4/api/_as_gen/matplotlib.figure.Figure.html
        """
        self.__figure = plt.figure(num = id, figsize = figsize, dpi = dpi,\
            facecolor = facecolor, edgecolor = edgecolor,\
            frameon = frameon, clear = clear)
        return self.__figure
# ------------------------------------------------------------------------------
    def close(self):
        """
        关闭对象：
        输入参数：
        返回参数：
        说明：调用该方法将关闭绘图对象并释放内存。
        参考：https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html
        """
        plt.close()
# ------------------------------------------------------------------------------
    def show(self):
        """
        显示绘图：
        输入参数：
        返回参数：
        说明：调用该方法将显示绘图figure。
        参考：https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html
        """
        # 自动调整边距，防止子图重叠
        self.__figure.tight_layout()
        self.__figure.show()
# ------------------------------------------------------------------------------
    def savefig(self, path):
        """
        保存绘图：
        输入参数：path 存储路径
        返回参数：
        说明：调用该方法将绘图figure保存为文件，保存路径由path指定。
        参考：https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
        """
        try:
            # 自动调整边距，防止子图重叠
            self.__figure.tight_layout()
            self.__figure.savefig(path)
        except:
            print("%s not exist" % self.dirname(path))
# ------------------------------------------------------------------------------
    @staticmethod
    def imread(self, path):
        """
        读取图像文件：
        输入参数：
        返回参数：image 图像数据
        说明：调用该方法将读取图像文件，并返回读取到的图像数据image。
        参考：https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html
        https://matplotlib.org/stable/api/image_api.html
        """
        image = img.imread(path)
        return image
# ------------------------------------------------------------------------------
    @staticmethod
    def imshow(self, image):
        """
        显示图像：
        输入参数：image 图像数据
        返回参数：
        说明：调用该方法将显示图像image。
        参考：https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html
        https://matplotlib.org/stable/api/image_api.html
        """
        plt.imshow(image) # 显示图片
        plt.axis('off')   # 不显示坐标轴
        plt.show()
# ------------------------------------------------------------------------------
    def label(self, xlabel = None, ylabel = None):
        """
        添加坐标轴标签：
        输入参数：(xlabel = None, ylabel = None) x轴、y轴标签
        返回参数：
        说明：调用该方法将给坐标轴添加标签，支持中文。
        参考：https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
        """
        if(xlabel != None):
            plt.xlabel(xlabel)
        if(ylabel != None):
            plt.ylabel(ylabel)
# ------------------------------------------------------------------------------
    def title(self, label):
        """
        添加标题：
        输入参数：label 标题
        返回参数：
        说明：调用该方法给绘图添加标题，支持中文。
        参考：https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html
        """
        return plt.title(label)
# ------------------------------------------------------------------------------
    def axis(self):
        """
        绘制坐标轴：
        输入参数：
        返回参数：
        说明：调用该方法将在绘图figure上绘制坐标轴。
        参考：https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html
        """
        # plt.axis["xzero"].set_visible(True)
        # plt.axis["xzero"].label.set_text("新建y=0坐标")
        # plt.axis["xzero"].label.set_color('green')
# ------------------------------------------------------------------------------
    def grid(self):
        """
        绘制网格线：
        输入参数：
        返回参数：
        说明：调用该方法将在绘图figure上绘制网格线。
        参考：https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html
        """
        return plt.grid(True)
# ------------------------------------------------------------------------------
    def legend(self, *args, **kwargs):
        """
        绘制图例：
        输入参数：
        返回参数：
        说明：调用该方法将在绘图figure上绘制图例。
        参考：https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
        """
        return plt.legend(*args, **kwargs)
# ------------------------------------------------------------------------------
    def subplot(self, subtitle):
        """
        绘制子图：
        输入参数：subtitle 子图标题
        返回参数：
        说明：调用该方法绘制子图。
        参考：https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html
        """
        return plt.subplot(subtitle)
# ------------------------------------------------------------------------------
    def subplots(self, nrows=1, ncols=1):
        """
        绘制子图：
        输入参数：
        返回参数：
        说明：调用该方法绘制子图。
        参考：https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html
        """
        return plt.subplots(nrows = nrows, ncols = ncols)
# ------------------------------------------------------------------------------
    @staticmethod
    def point(self, x, y, size = None, color = None, marker = None):
        """
        获取一个点对象：
        输入参数：(x, y, size = None, color = None, marker = None) x、y、大小、颜色、形状
        返回参数：point
        说明：调用该方法将获取一个点对象，点的坐标（x、y）是必须的，其他可选。
        """
        point = {'x':x, 'y':y, 'size':size, 'color':color, 'marker':marker}
        return point
# ------------------------------------------------------------------------------
    @staticmethod
    def points(self, x, y, size = None, color = None, marker = None):
        """
        获取多个点对象：
        输入参数：(x, y, size = None, color = None, marker = None) x、y、大小、颜色、形状
        返回参数：points
        说明：调用该方法将获取一个点对象，点的坐标（x、y）是必须的，其他可选。
        """
        assert type(x) is list or type(x) is tuple, "type {} is not list or tuple".format(type(x))
        assert type(y) is list or type(y) is tuple, "type {} is not list or tuple".format(type(y))
        assert len(x) == len(y), "x length : {} not equal to y length : {}".format(len(x), len(y))
        points = []
        for i in range(len(x)):
            points.append({'x':x[i], 'y':y[i], 'size':size, 'color':color, 'marker':marker})
        return points
# ------------------------------------------------------------------------------
    def xybar(self, x, y, color = None, align = None):
        """
        绘制条形图：
        输入参数：(x, y, size = None, color = None, marker = None) x、y、大小、颜色、形状
        返回参数：
        说明：调用该方法将绘制条形图。
        参考：https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html
        """
        plt.bar(x = x, y = y)
# ------------------------------------------------------------------------------
    def xyplot(self, x, y, *args, **kwargs):
        """
        绘制折线图：
        输入参数：(x, y, color = None, linewidth = None, linestyle = None, label = None) x、y、颜色、线宽、线型、标签
        返回参数：
        说明：调用该方法将绘制折线图。
        参考：https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
        """
        return plt.plot(x, y, *args, **kwargs)
# ------------------------------------------------------------------------------
    def plot(self, points, *args, **kwargs):
        """
        绘制折线图：
        输入参数：(points, color = None, linewidth = None, linestyle = None, label = None) 点、颜色、线宽、线型、标签
        返回参数：
        说明：调用该方法将绘制折线图。
        参考：https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
        """
        xp = []
        yp = []
        for point in points:
            xp.append(point['x'])
            yp.append(point['y'])
        return plt.plot(xp, yp, *args, **kwargs)
# ------------------------------------------------------------------------------
    def xyscatter(self, x, y, size = None, color = None, marker = None):
        """
        绘制散点图：
        输入参数：(x, y, size = None, color = None, marker = None) x、y、大小、颜色、形状
        返回参数：
        说明：调用该方法将绘制散点图。
        参考：https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
        """
        plt.scatter(x = x, y = y, s = size, c = color, marker = marker)
# ------------------------------------------------------------------------------
    def scatter(self, points):
        """
        绘制散点图：
        输入参数：points 可以是一个点对象，或是几个点对象组成的集合（列表or元组）
        返回参数：
        说明：调用该方法将绘制散点图。
        参考：https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
        """
        if(type(points) == dict):
            plt.scatter(points['x'], points['y'], s = points['size'],
            c = points['color'], marker = points['marker'])
        elif(type(points) == list or type(points) == tuple):
            xs = []
            ys = []
            ss = []
            cs = []
            ms = []
            for i in range(len(points)):
                point = points[i]
                xs.append(point['x'])
                ys.append(point['y'])
                if ss != None:
                    if point['size'] != None:
                        ss.append(point['size'])
                    else:
                        ss = None
                if cs != None:
                    if point['color'] != None:
                        cs.append(point['color'])
                    else:
                        cs = None
                if ms != None:
                    if point['marker'] != None:
                        ms.append(point['marker'])
                    else:
                        ms = None
            plt.scatter(x = xs, y = ys, s = ss, c = cs, marker = ms)
# ------------------------------------------------------------------------------
