#!/usr/bin/env python

import unittest

from pybank.cbs import CBS

class TestGetMessageLength(unittest.TestCase):
    
    def setUp(self):
        self.cbs = CBS(host=None, port=None)

    def test_get_message_length_ascii_empty(self):
        self.assertEqual(self.cbs.get_message_length(b''), b'\x00\x00')
 
    def test_get_message_length_ascii_XX(self):
        self.assertEqual(self.cbs.get_message_length(b'XX'), b'\x00\x02')

    def test_get_message_length_ascii_length_28(self):
        self.assertEqual(self.cbs.get_message_length(b'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'), b'\x00\x28')

    def test_get_message_length_ascii_length_216(self):
        self.assertEqual(self.cbs.get_message_length(b'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'), b'\x02\x16')


class TestGetBalanceString(unittest.TestCase):
    def setUp(self):
        self.cbs = CBS(host=None, port=None)

    def test_get_balance_string_empty(self):
        self.assertEqual(self.cbs.get_balance_string('', ''), '')

    def test_get_balance_string_positive(self):
        self.assertEqual(self.cbs.get_balance_string('1234.56', '643'), '016C000000123456643')

    def test_get_balance_string_negative(self):
        self.assertEqual(self.cbs.get_balance_string('-1234.59', '826'), '016D000000123459826')

    def test_get_balance_string_unstripped(self):
        self.assertEqual(self.cbs.get_balance_string('  -1234.59 ', '840'), '016D000000123459840')

if __name__ == '__main__':
    unittest.main()