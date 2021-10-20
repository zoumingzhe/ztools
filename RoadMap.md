RoadMap
=======

时间表：
 - 2021/08/22 新增csv类测试
 - 2021/08/20 新增并实现csv类

# common
## file
 - [BUG]scan输出tuple类型其他函数不支持
 - 增加join方法并使用join方法重写路径拼接get_path
 - 使用format方法生成字符串
 - copy、move、rename、remove同时支持文件和文件夹操作
 - ensure移除isCreate参数
 - scan以tree结构（{'dirs:' : [], 'files' : []}）返回结果并重命名为tree
 - 通过锁以保证并发性
## sheet
### sheet
表单基类。
 - 表单集（sheets）增删表单（sheet）
 - 表单（sheet）增删行（row）
 - sheet属性：sheet(i).index、sheet(i).name、sheet(i).rows、sheet(i).col.width

### csv (Comma-Separated Values)
逗号分隔值文件格式，有时也称为字符分隔值，因为分隔字符也可以不是逗号。
 - 已支持 逗号分隔的.csv读写
 - 指定分割符号

### xls - excel files
参考 [Working with Excel Files in Python](http://www.python-excel.org/) 页面
 - 已支持 [xlrd](https://xlrd.readthedocs.io/en/latest/)
 - 已支持 [xlwt](https://xlwt.readthedocs.io/en/latest/)
 - 待支持 [openpyxl](https://openpyxl.readthedocs.io/en/stable/)

# gui
## plot
### plot
 - title        标题
 - suptitle     子标题
 - axis         坐标轴
 - xlim
 - ylim
 - label        坐标轴标注
 - tick         刻度线
 - tick label   刻度线注释
 - legend       图例                    DONE
