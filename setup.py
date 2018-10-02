# setup.py for PyTools
#
# Direct install (all systems):
#   "python setup.py install"
#
# For Python 3.x use the corresponding Python executable,
# e.g. "python3 setup.py ..."
#
# (C) 2018 ZouMingzhe <zoumingzhe@qq.com>
#
# SPDX-License-Identifier:    MIT

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="PyTools",
    description="ToolBox for Python, Easy to Use.",
    version="1.0",
    author="Zou Mingzhe",
    author_email="zoumingzhe@qq.com",
    url="https://zoumingzhe.github.io/",
    packages=['PyTools'],
    license="MIT",
    long_description=open('README.rst', mode='r', encoding='UTF-8').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: Chinese',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Tool',
        'Topic :: Timeout',
        'Topic :: ProgressBar',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms='any',
)