依以下步骤发布到PyPI（https://pypi.org）：
1.修改元数据
    1a.修改源代码
    1b.文件“../ztools/__init__.py”（如有新增import对象）
    1c.文件“../setup.py”中的版本号
2.检查是否安装twine、wheel模块（python -m pip list）
    如果未安装，请依次执行以下命令：
        >>>python -m pip install --upgrade pip
        >>>python -m pip install twine
        >>>python -m pip install wheel
3.打包及上传，依次执行以下脚本文件：
    windows:
        ./windows/step1.打包.bat
        ./windows/step2.上传.bat
    linux:
        ./linux/step1.打包.sh
        ./linux/step2.上传.sh
4.安装、升级、卸载ztools模块
    可使用dist目录下的whl包进行本地测试
    安装ztools模块：
        >>>python -m pip install ztools
        >>>python -m pip list
    升级ztools模块
        >>>python -m pip install --upgrade ztools
        >>>python -m pip list
    卸载ztools模块
        >>>python -m pip uninstall ztools
        >>>python -m pip list
5.以下目录为打包时自动生成：
    ../build
    ../dist
    ../ztools.egg-info
