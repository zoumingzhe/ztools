#!/usr/bin/env python3
import sys
sys.path.append(r'..\..\..\ztools\ztools')
from common.hash import hash
import hashlib

import unittest
from unittest import mock

class test_hash(unittest.TestCase):
    def test_hash_handle(self):
        md5 = hash.md5()
        md5.update(b'unittest')
        self.assertEqual(md5.hexdigest(), '16802231b09f155b7a42a5dcaba33a74')
        sha1 = hash.sha1()
        sha1.update(b'unittest')
        self.assertEqual(sha1.hexdigest(), '94e060874450b5ea724bb6ce5ca7be4f6a73416b')

    def test_hash_bytes(self):
        self.assertEqual(hash.md5(b'unittest'), '16802231b09f155b7a42a5dcaba33a74')
        self.assertEqual(hash.sha1(b'unittest'), '94e060874450b5ea724bb6ce5ca7be4f6a73416b')

    def test_hash_string(self):
        self.assertEqual(hash.md5('nihao', encode='ascii'), '194ce5d0b89c47ff6b30bfb491f9dc26')
        self.assertEqual(hash.sha1('nihao', encode='ascii'), '23fcf96d70494b81c5084c0da6a6e8d84a9c5d20')
        self.assertEqual(hash.md5('你好', encode='utf-8'), '7eca689f0d3389d9dea66ae112e5cfd7')
        self.assertEqual(hash.sha1('你好', encode='utf-8'), '440ee0853ad1e99f962b63e459ef992d7c211722')
        self.assertEqual(hash.md5('你好', encode='gb2312'), 'b94ae3c6d892b29cf48d9bea819b27b9')
        self.assertEqual(hash.sha1('你好', encode='gb2312'), '4bd9abaa33ea0834383e15fef9ae377f762fc03b')

    def test_hash_file(self):
        self.assertEqual(hash.md5(filepath='ts_file.a'), '76027eec48992dcba5b3b73844a03105')
        self.assertEqual(hash.sha1(filepath='ts_file.a'), '2d6888a7f2dc0f1adabc691d7f1ba01786a48fb5')
        self.assertEqual(hash.md5(filepath='ts_file.b'), '1a8cbbcae05340c2dc5dee5199ad8401')
        self.assertEqual(hash.sha1(filepath='ts_file.b'), '9db1d4c65e3e154451b467fc9e3fbea5f8e43221')


if __name__ == '__main__':
    unittest.main()
