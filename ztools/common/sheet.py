# coding=utf-8
# ------------------------------------------------------------------------------
# 类 csv
# ------------------------------------------------------------------------------
# 变更履历：
# 2021-08-20 | Zou Mingzhe   | Ver0.1  | 初始版本
# ------------------------------------------------------------------------------
# MAP：
# 待测试 | read(...)                    | 读
# 待测试 | write(...)                   | 写
# ------------------------------------------------------------------------------
class csv():
    """
    csv类提供了对.csv文件的操作。
    """
    def __init__(self):
        self.__version = "0.1"
# ------------------------------------------------------------------------------
    @staticmethod
    def read(csvfile, cleanblank = True):
        with open(csvfile, 'r', newline = None) as f:
            sheet = []
            for eachline in f:
                row = [ e.strip() for e in eachline.split(',') ]
                if cleanblank and row == ['']:
                    continue
                sheet.append(row)
            return sheet
# ------------------------------------------------------------------------------
    @staticmethod
    def write(csvfile, sheet):
        with open(csvfile, 'w', newline = None) as f:
            for row in sheet:
                f.write(", ".join([str(e) for e in row]))
                f.write("\n")
            return True
        return False
# ------------------------------------------------------------------------------



# ------------------------------------------------------------------------------
# 类 xls
# ------------------------------------------------------------------------------
# 变更履历：
# 2019-05-02 | Zou Mingzhe   | Ver0.2  | 1.增加 WriteFile(self, book, path)
# 2019-04-14 | Zou Mingzhe   | Ver0.1  | 初始版本
# ------------------------------------------------------------------------------
# MAP：
# 未测试 | ReadInfo(self, ...)          | 读
# 未测试 | ReadObj(self, ...)           | 读
# 未测试 | ReadObjMulti(self, ...)      | 读
# 未测试 | WriteFile(self, ...)         | 写
# 未测试 | WriteObj(self, ...)          | 写
# 未测试 | WriteObjMulti(self, ...)     | 写
# ------------------------------------------------------------------------------
from .file import fbasic
import xlrd
import xlwt
# ------------------------------------------------------------------------------
class xls(fbasic):
    """
    xls类提供了对.xls文件的操作。
    """
    def __init__(self):
        self.__version = "0.2"
# ------------------------------------------------------------------------------
    @staticmethod
    def ReadInfo(xls_file):
        book = xlrd.open_workbook(xls_file)
        sheets = book.sheet_names()
        info = sheets
        return info
# ------------------------------------------------------------------------------
    @staticmethod
    def ReadObj(xls_file, sheet_index):
        book = xlrd.open_workbook(xls_file)
        sheet0 = book.sheet_by_index(sheet_index)
        nrows = sheet0.nrows
        info = []
        for i in range(nrows):
            info.append(sheet0.row_values(i))
        return info
# ------------------------------------------------------------------------------
    @staticmethod
    def ReadObjMulti(xls_file):
        book = xlrd.open_workbook(xls_file)
        sheets = book.sheet_names()
        info = []
        for sheet_index in range(len(sheets)):
            sheet0 = book.sheet_by_index(sheet_index)
            nrows = sheet0.nrows
            ainfo = []
            for i in range(nrows):
                ainfo.append(sheet0.row_values(i))
            info.append(ainfo)
        return info
# ------------------------------------------------------------------------------
    @staticmethod
    def WriteFile(book, path):
        try:
            fbasic.ensure(fbasic.dirname(path))
            book.save(path)
        except e as error:
            print("Excel文件\"%s\"保存失败，请检查路径是否正确、文件是否关闭！" % path)
# ------------------------------------------------------------------------------
    @staticmethod
    def WriteObj(xls_file, sheet_name, obj, width_auto = True):
        # 创建Workbook对象
        book = xlwt.Workbook(encoding='utf-8', style_compression=0)
        # 创建sheet对象
        sheet = book.add_sheet(sheet_name, cell_overwrite_ok=True)
        # 写数据
        cwidth = []
        for i in range(len(obj)):
            for j in range(len(obj[i])):
                sheet.write(i, j, obj[i][j])
                if width_auto == True:
                    # 宽度自适应
                    awidth = len(str(obj[i][j]).encode('gbk'))
                    if j >= len(cwidth):
                        cwidth.append(0)
                        sheet.col(j).width = 325
                    if awidth > cwidth[j]:
                        cwidth[j] = awidth
                        sheet.col(j).width = 325 * cwidth[j]
        # 保存
        xls.WriteFile(book, xls_file)
# ------------------------------------------------------------------------------
    @staticmethod
    def WriteObjMulti(xls_file, sheet_name, obj, width_auto = True):
        # 创建Workbook对象
        book = xlwt.Workbook(encoding='utf-8', style_compression=0)
        x = type(sheet_name)
        if x is list or x is tuple:
            for n in range(len(sheet_name)):
                # 创建sheet对象
                sheet = book.add_sheet(sheet_name[n], cell_overwrite_ok=True)
                # 写数据
                cwidth = []
                for r in range(len(obj[n])):
                    for c in range(len(obj[n][r])):
                        sheet.write(r, c, obj[n][r][c])
                        if width_auto == True:
                            # 宽度自适应
                            awidth = len(str(obj[n][r][c]).encode('gbk'))
                            if c >= len(cwidth):
                                cwidth.append(0)
                                sheet.col(c).width = 325
                            if awidth > cwidth[c]:
                                cwidth[c] = awidth
                                sheet.col(c).width = 325 * cwidth[c]
        else:
            sheet = book.add_sheet(sheet_name, cell_overwrite_ok=True)
            cwidth = []
            for r in range(len(obj)):
                for c in range(len(obj[r])):
                    element = obj[r][c]
                    sheet.write(r, c, element)
                    if width_auto == True:
                        awidth = len(str(element).encode('gbk'))
                        if c >= len(cwidth):
                            cwidth.append(0)
                            sheet.col(c).width = 325
                        if awidth > cwidth[c]:
                            cwidth[c] = awidth
                            sheet.col(c).width = 325 * cwidth[c]
        # 保存
        xls.WriteFile(book, xls_file)
# ------------------------------------------------------------------------------
