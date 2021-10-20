import os
import sys
sys.path.append(r'..\..\..\ztools\ztools')
from common.file import fbasic

import unittest
from unittest import mock

class test_fbasic(unittest.TestCase):
    def test_fbasic_join(self):
        self.assertEqual(fbasic.join('.', 'test'), r'.\test')
        self.assertEqual(fbasic.join('..', 'demo'), r'..\demo')
        self.assertEqual(fbasic.join('...', 'test', 'demo'), r'...\test\demo')
        self.assertEqual(fbasic.join(dirname='.'), r'.')
        self.assertEqual(fbasic.join('test', dirname='.'), r'.\test')
        self.assertEqual(fbasic.join('test', 'demo', dirname='.'), (r'.\test', r'.\demo'))

    def test_fbasic_basename(self):
        result = fbasic.basename(r'.\demo.txt',)
        self.assertEqual(result, 'demo.txt')
        result = fbasic.basename(r'\home\test\demo.txt',)
        self.assertEqual(result, 'demo.txt')

    def test_fbasic_dirname(self):
        result = fbasic.dirname(r'.\demo.txt',)
        self.assertEqual(result, r'.')
        result = fbasic.dirname(r'\home\test\demo.txt',)
        self.assertEqual(result, r'\home\test')

    def test_fbasic_folder(self):
        srcpath = fbasic.join('.', 'folder', 'temp', 'test', 'src')
        dstpath = fbasic.join('.', 'folder', 'temp', 'test', 'dst')
        if os.path.exists(srcpath):
            self.assertTrue(fbasic.remove(srcpath))
        if os.path.exists(dstpath):
            self.assertTrue(fbasic.remove(dstpath))
        self.assertFalse(os.path.exists(srcpath))
        self.assertFalse(os.path.exists(dstpath))
        # create
        self.assertTrue(fbasic.ensure(srcpath))
        self.assertTrue(os.path.isdir(srcpath))
        self.assertFalse(os.path.isdir(dstpath))
        # move
        self.assertTrue(fbasic.move(srcpath, dstpath))
        self.assertFalse(os.path.isdir(srcpath))
        self.assertTrue(os.path.isdir(dstpath))
        # copy
        self.assertTrue(fbasic.copy(dstpath, srcpath))
        self.assertTrue(os.path.isdir(srcpath))
        self.assertTrue(os.path.isdir(dstpath))
        # remove
        self.assertTrue(fbasic.remove(dstpath))
        self.assertTrue(os.path.exists(srcpath))
        self.assertFalse(os.path.exists(dstpath))
        # rename
        self.assertTrue(fbasic.rename(srcpath, dstpath))
        self.assertFalse(os.path.isdir(srcpath))
        self.assertTrue(os.path.isdir(dstpath))
        # remove
        self.assertTrue(fbasic.remove(dstpath))
        self.assertFalse(os.path.exists(srcpath))
        self.assertFalse(os.path.exists(dstpath))

    def test_fbasic_file(self):
        dirpath = fbasic.join('.', 'folder', 'temp')
        self.assertTrue(fbasic.ensure(dirpath))
        self.assertTrue(os.path.isdir(dirpath))
        srcpath = fbasic.join(dirpath, 'src.tmp')
        dstpath = fbasic.join(dirpath, 'dst.tmp')
        if os.path.exists(srcpath):
            self.assertTrue(fbasic.remove(srcpath))
        if os.path.exists(dstpath):
            self.assertTrue(fbasic.remove(dstpath))
        self.assertFalse(os.path.exists(srcpath))
        self.assertFalse(os.path.exists(dstpath))
        # copy
        self.assertTrue(os.path.isfile(fbasic.join('.', 'folder', 'demo.txt')))
        self.assertTrue(fbasic.copy(fbasic.join('.', 'folder', 'demo.txt'), srcpath))
        self.assertTrue(os.path.isfile(srcpath))
        self.assertFalse(os.path.isfile(dstpath))
        # move
        self.assertTrue(fbasic.move(srcpath, dstpath))
        self.assertFalse(os.path.isfile(srcpath))
        self.assertTrue(os.path.isfile(dstpath))
        # rename
        self.assertTrue(fbasic.rename(dstpath, srcpath))
        self.assertTrue(os.path.isfile(srcpath))
        self.assertFalse(os.path.isfile(dstpath))
        # remove
        self.assertTrue(fbasic.remove(srcpath))
        self.assertFalse(os.path.exists(srcpath))
        self.assertFalse(os.path.exists(dstpath))

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
