import sys
sys.path.append(r'..\..\..\ztools\ztools')
from common.sheet import csv

import unittest
from unittest import mock

class testcsv(unittest.TestCase):
    def test_csv_read_cleanblank(self):
        result = csv.read(r'.\ts_csv_input.csv', cleanblank = True)
        expect = [
            ['A', 'B', 'C', 'D', 'E'], 
            ['a', '', 'b', 'c', ''], 
            ['a', '', 'b', 'c', ''], 
            ['A', '', 'B', '', 'C'], 
            ['1', '', '2', '', '3'], 
            ['a', 'b', 'c', 'd', 'e'], 
            ['1', '2', '3', '4', '5', ''], 
            ['a', '2', 'b', '4', '', ''], 
            ['abc 123', '', 'ABC abc', '123   ABC', '', ''], 
            ['abc \t123', '', 'ABC\t abc', '123 \t ABC', '', ''], 
            ['abc\t\t123', '', 'ABC\t \tabc', '123 \t \t ABC', '', ''], 
            ['abc \t \t 123', '', 'ABC\t \t abc', '123 \t \tABC', '', ''], 
            ['abc\t123', '', 'ABC\t\tabc', '123\t\t\tABC', '', ''], 
        ]
        self.assertEqual(result, expect)

    def test_csv_read_no_cleanblank(self):
        result = csv.read(r'.\ts_csv_input.csv', cleanblank = False)
        expect = [
            ['A', 'B', 'C', 'D', 'E'], 
            [''], 
            ['a', '', 'b', 'c', ''], 
            [''], 
            ['a', '', 'b', 'c', ''], 
            [''], 
            ['A', '', 'B', '', 'C'], 
            [''], 
            ['1', '', '2', '', '3'], 
            [''], 
            ['a', 'b', 'c', 'd', 'e'], 
            [''], 
            ['1', '2', '3', '4', '5', ''], 
            [''], 
            ['a', '2', 'b', '4', '', ''], 
            [''], 
            ['abc 123', '', 'ABC abc', '123   ABC', '', ''], 
            ['abc \t123', '', 'ABC\t abc', '123 \t ABC', '', ''], 
            ['abc\t\t123', '', 'ABC\t \tabc', '123 \t \t ABC', '', ''], 
            ['abc \t \t 123', '', 'ABC\t \t abc', '123 \t \tABC', '', ''], 
            ['abc\t123', '', 'ABC\t\tabc', '123\t\t\tABC', '', ''], 
        ]
        self.assertEqual(result, expect)

if __name__ == '__main__':
    unittest.main()
