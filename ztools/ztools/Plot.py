#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
# 类 Plot
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2019-04-20 | Zou Mingzhe   | Ver0.6  | 1.修改 Scatter(self, point)，输入的point类型支持list或者tuple
# 2019-04-15 | Zou Mingzhe   | Ver0.5  | 1.完善帮助信息
# 2019-02-11 | Zou Mingzhe   | Ver0.4  | 1.增加 Save(self, path)
#            |               |         | 2.增加 Read(self, path)
#            |               |         | 3.增加 ShowImage(self, image)
# 2019-01-28 | Zou Mingzhe   | Ver0.3  | 1.增加 Grid(self)
#            |               |         | 2.增加 Point(self, x, y, size = None, color = None, marker = None)
#            |               |         | 3.修改 Scatter(self, point)
# 2018-11-21 | Zou Mingzhe   | Ver0.2  | 1.增加 Show(self)
#            |               |         | 2.增加 Label(self, xlabel = None, ylabel = None)
#            |               |         | 3.增加 Scatter(self, x, y)
# 2018-11-19 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | Version(self, ...)  | 版本显示
# 已测试 | Save(self, ...)     | 保存绘图
# 已测试 | Read(self, ...)     | 读取文件
# 已测试 | Show(self)          | 显示绘图
# 已测试 | ShowImage(self, ...)| 显示图像
# 已测试 | Label(self, ...)    | 添加坐标轴标签
# 已测试 | Grid(self)          | 绘制网格线
# 已测试 | Point(self, ...)    | 获取一个点对象
# 已测试 | Scatter(self, ...)  | 绘制散点图
# ----------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import matplotlib.image  as img
import ztools.File       as fil
# ----------------------------------------------------------------------------------------------------
class Plot(fil):
    """
    Plot类提供了绘图功能，它是基于matplotlib的，同时也是matplotlib的增强。
    只需要几行代码即可获得绘制图形，大大缩减了绘图的代码行数，获得高质量的编程体验。
    特性：
    1、对matplotlib功能进行整合，简单易用；
    2、支持中文，直接支持标题、坐标轴、图例等的中文显示；
    3、使用Scatter绘制散点图时，使用“点对象”作为参数，而不需要多个“向量”参数，并通过Point进一步简化了点的创建。
    """
    def __init__(self, title, size = None):
        self.__version = "0.6"
        self.__title   = title
        self.__figure  = plt.figure(num = self.__title, figsize = size)
        plt.title(self.__title)
        plt.rcParams['font.sans-serif']=['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False    # 用来正常显示负号
        # 有中文出现的情况，需要u'内容'
# ----------------------------------------------------------------------------------------------------
    def Version(self, isShow = False):
        """
        版本显示：
        输入参数：isShow = False
        返回参数：self.__version
        说明：调用该方法将返回类的版本号，若isShow == True则会在屏幕上打印版本号。
        """
        if(isShow):
            print("[ztools]-[Plot]-[vesion:%s]" % self.__version)
        return self.__version
# ----------------------------------------------------------------------------------------------------
    def Save(self, path):
        """
        保存绘图：
        输入参数：path 存储路径
        返回参数：
        说明：调用该方法将绘图figure保存为文件，保存路径由path指定。
        """
        try:
            fig = plt.figure(self.__title)
            fig.savefig(path)
        except:
            print("%s not exist" % self.a_folder(path))
# ----------------------------------------------------------------------------------------------------
    def Read(self, path):
        """
        读取文件：
        输入参数：
        返回参数：image 图像数据
        说明：调用该方法将读取图像文件，并返回读取到的图像数据image。
        """
        image = img.imread(path)
        return image
# ----------------------------------------------------------------------------------------------------
    def Show(self):
        """
        显示绘图：
        输入参数：
        返回参数：
        说明：调用该方法将显示绘图figure。
        """
        plt.figure(self.__title)
        plt.show()
# ----------------------------------------------------------------------------------------------------
    def ShowImage(self, image):
        """
        显示图像：
        输入参数：image 图像数据
        返回参数：
        说明：调用该方法将显示图像image。
        """
        plt.imshow(image) # 显示图片
        plt.axis('off')   # 不显示坐标轴
        plt.show()
# ----------------------------------------------------------------------------------------------------
    def Label(self, xlabel = None, ylabel = None):
        """
        添加坐标轴标签：
        输入参数：(xlabel = None, ylabel = None) x轴、y轴标签
        返回参数：
        说明：调用该方法并传入参数将给坐标轴添加标签，默认不添加，支持中文。
        """
        plt.figure(self.__title)
        if(xlabel != None):
            plt.xlabel(xlabel)
        if(ylabel != None):
            plt.ylabel(ylabel)
# ----------------------------------------------------------------------------------------------------
    def Axis(self):
        """
        绘制坐标轴：
        输入参数：
        返回参数：
        说明：调用该方法将在绘图figure上绘制坐标轴。
        """
        plt.figure(self.__title)
        # plt.axis["xzero"].set_visible(True)
        # plt.axis["xzero"].label.set_text("新建y=0坐标")
        # plt.axis["xzero"].label.set_color('green')
# ----------------------------------------------------------------------------------------------------
    def Grid(self):
        """
        绘制网格线：
        输入参数：
        返回参数：
        说明：调用该方法将在绘图figure上绘制网格线。
        """
        plt.figure(self.__title)
        plt.grid(True)
# ----------------------------------------------------------------------------------------------------
    def Point(self, x, y, size = None, color = None, marker = None):
        """
        获取一个点对象：
        输入参数：(x, y, size = None, color = None, marker = None) x、y、大小、颜色、形状
        返回参数：point
        说明：调用该方法将获取一个点对象，点的坐标（x、y）是必须的，其他可选。
        """
        point = {'x':x, 'y':y, 'size':size, 'color':color, 'marker':marker}
        return point
# ----------------------------------------------------------------------------------------------------
    def Scatter(self, point):
        """
        绘制散点图：
        输入参数：point 可以是一个点对象，或是几个点对象组成的集合（列表or元组）
        返回参数：
        说明：调用该方法将绘制散点图。
        """
        plt.figure(self.__title)
        if(type(point) == dict):
            plt.scatter(x = point['x'], y = point['y'], s = point['size'],
            c = point['color'], marker = point['marker'])
        elif(type(point) == list or type(point) == tuple):
            for i in range(len(point)):
                onepoint = point[i]
                plt.scatter(x = onepoint['x'], y = onepoint['y'], s = onepoint['size'],
                c = onepoint['color'], marker = onepoint['marker'])
# ----------------------------------------------------------------------------------------------------
