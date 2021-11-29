# coding=utf-8
# ------------------------------------------------------------------------------
# 类 progressbar
# ------------------------------------------------------------------------------
# 变更履历：
# 2021-02-27 | Zou Mingzhe   | Ver0.3  | 1.删除 Version(self, isShow = False)
#            |               |         | 2.修改 Percent(self, ...) 为 percent(self, ...)
#            |               |         | 3.修改 Number(self, ...)  为 number(self, ...)
# 2019-05-03 | Zou Mingzhe   | Ver0.2  | 1.增加 EOF(self, clear = False)
#            |               |         | 2.修改 PercentProgressBar(self, ...) 为 Percent(self, ...)
#            |               |         | 3.修改 NumberProgressBar(self, ...)  为 Number(self, ...)
# 2018-09-05 | Zou Mingzhe   | Ver0.1  | 初始版本
# ------------------------------------------------------------------------------
# MAP：
# 已测试 | percent(self, ...)           | 百分比进度条
# 已测试 | number(self, ...)            | 数字进度条
# 已测试 | EOF(self, ...)               | 结束符
# ------------------------------------------------------------------------------
import sys
# ------------------------------------------------------------------------------
class progressbar:
    """
    progressbar类提供了进度条字符串。
    """
    def __init__(self):
        self.__version = "0.3"
        self.__progress = 0
        self.__maxlength = 0
        self.__barlist = ['', '▏', '▎', '▍', '▌', '▋', '▊', '▉', '█', '█']
# ------------------------------------------------------------------------------
    def percent(self, progress, title = None, show = False):
        """
        百分比进度条：
        输入参数：progress, show = False
        返回参数：string
        说明：调用该方法将返回百分比进度条，百分比进度条 = 百分比 + 进度条。progress必须介于0至1之间。
        """
        progress = progress * 100
        if(progress > 100):
            progress = 100
        elif(progress < 0):
            progress = 0
        self.__progress = progress
        strbar = '█'*int(progress / 10) + self.__barlist[int(progress) % 10]
        string = (str('%s:'%title) if title else '') + str('%.2f%% %s' % (progress, strbar))
        self.__maxlength = max(len(string), self.__maxlength)
        if(show):
            sys.stdout.write(string + '\r')
            sys.stdout.flush()
        return string
# ------------------------------------------------------------------------------
    def number(self, done, sum, title = None, show = False):
        """
        数字进度条：
        输入参数：done, sum, show = False
        返回参数：string
        说明：调用该方法将返回数字进度条，数字进度条 = done/sum + 进度条。
        其中，done为已完成进度，sum为总进度。
        """
        if(sum <= 0):
            sum = 1
        if(done < 0):
            done = 0
        if(done > sum):
            done = sum
        progress = done * 100 / sum
        if(progress > 100):
            progress = 100
        elif(progress < 0):
            progress = 0
        self.__progress = progress
        strbar = '█'*int(progress / 10) + self.__barlist[int(progress) % 10]
        string = (str('%s:'%title) if title else '') + str('%.2f%% (%d/%d) %s' % (progress, done, sum, strbar))
        self.__maxlength = max(len(string), self.__maxlength)
        if(show):
            sys.stdout.write(string + '\r')
            sys.stdout.flush()
        return string
# ------------------------------------------------------------------------------
    def EOF(self, clear = False):
        """
        结束符：
        输入参数：clear = False
        返回参数：
        说明：调用该方法将换行或清空屏幕进度条。
        """
        if(clear):
            for n in range(self.__maxlength):
                sys.stdout.write(' ')
                sys.stdout.flush()
            sys.stdout.write('\r')
            sys.stdout.flush()
        else:
            sys.stdout.write('\n')
            sys.stdout.flush()
        self.__maxlength = 0
# ------------------------------------------------------------------------------
