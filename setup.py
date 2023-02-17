# setup.py for ztools
#
# Direct install (all systems):
#   "python setup.py install"
#
# For Python 3.x use the corresponding Python executable,
# e.g. "python3 setup.py ..."
#
# (C) 2018-2023 ZouMingzhe <zoumingzhe@qq.com>
#
# SPDX-License-Identifier:    MIT

VERSION = "2.4.6"

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="ztools",
    license="MIT",
    version=VERSION,
    author="Zou Mingzhe",
    author_email="zoumingzhe@qq.com",
    url="https://github.com/zoumingzhe/ztools",
    description="ToolBox for Python, Easy to Use.",
    packages=[
        'ztools',
        'ztools.common',
        'ztools.db',
        'ztools.ds',
        'ztools.gui',
        'ztools.utils',
    ],
    entry_points={
        'console_scripts': [
        ]
    },
    # long_description=open('.\README.rst', mode='r', encoding='UTF-8').read(),
    install_requires=[
        'psutil',
        'colorama',
        'matplotlib',
        'pymysql',
        'xlrd<=1.2.0',
        'xlwt',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Natural Language :: Chinese (Simplified)',
    ],
    platforms='any',
)