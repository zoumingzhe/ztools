import sys
sys.path.append(r'..\..\..\ztools\ztools')
from common.file import fbasic

import unittest
from unittest import mock

class test_fbasic(unittest.TestCase):
    def test_fbasic_get_name(self):
        result = fbasic.get_name(r'.\demo.txt',)
        self.assertEqual(result, 'demo.txt')
        result = fbasic.get_name(r'\home\test\demo.txt',)
        self.assertEqual(result, 'demo.txt')

    def test_fbasic_get_folder(self):
        result = fbasic.get_folder(r'.\demo.txt',)
        self.assertEqual(result, r'.')
        result = fbasic.get_folder(r'\home\test\demo.txt',)
        self.assertEqual(result, r'\home\test')

    def test_fbasic_scan(self):
        # only folder
        result = fbasic.scan(r'.\folder')
        expect = (
            r'.\folder\demo', 
            r'.\folder\demo.cfg', 
            r'.\folder\demo.exe', 
            r'.\folder\demo.file', 
            r'.\folder\demo.txt', 
        )
        self.assertEqual(result, expect)
        # subfolder
        result = fbasic.scan(r'.\folder', sub=True)
        expect = (
            r'.\folder\demo', 
            r'.\folder\demo.cfg', 
            r'.\folder\demo.exe', 
            r'.\folder\demo.file', 
            r'.\folder\demo.txt', 
            r'.\folder\subfolder\demo\demo',
            r'.\folder\subfolder\demo\demo.cfg',
            r'.\folder\subfolder\demo\demo.txt',
            r'.\folder\subfolder\demo\test',
            r'.\folder\subfolder\demo\test.cfg',
            r'.\folder\subfolder\demo\test.txt',
            r'.\folder\subfolder\subfolder',
            r'.\folder\subfolder\subfolder.cfg',
            r'.\folder\subfolder\subfolder.exe',
            r'.\folder\subfolder\subfolder.file',
            r'.\folder\subfolder\subfolder.txt',
        )
        self.assertEqual(result, expect)
        # prefix
        result = fbasic.scan(r'.\folder', sub=True, prefix='sub')
        expect = (
            r'.\folder\subfolder\subfolder',
            r'.\folder\subfolder\subfolder.cfg',
            r'.\folder\subfolder\subfolder.exe',
            r'.\folder\subfolder\subfolder.file',
            r'.\folder\subfolder\subfolder.txt',
        )
        self.assertEqual(result, expect)
        # postfix
        result = fbasic.scan(r'.\folder', sub=True, postfix='.cfg')
        expect = (
            r'.\folder\demo.cfg', 
            r'.\folder\subfolder\demo\demo.cfg',
            r'.\folder\subfolder\demo\test.cfg',
            r'.\folder\subfolder\subfolder.cfg',
        )
        self.assertEqual(result, expect)
        # prefix and postfix
        result = fbasic.scan(r'.\folder', sub=True, prefix='demo', postfix='.cfg')
        expect = (
            r'.\folder\demo.cfg', 
            r'.\folder\subfolder\demo\demo.cfg', 
        )
        self.assertEqual(result, expect)
        # prefix and postfix
        result = fbasic.scan(r'.\folder', sub=True, prefix='sub', postfix='.cfg')
        expect = (
            r'.\folder\subfolder\subfolder.cfg',
        )
        self.assertEqual(result, expect)
        # only file
        # only folder
        # file and folder
        # no file and folder

if __name__ == '__main__':
    unittest.main()
