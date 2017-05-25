#!/usr/bin/env python

import unittest
import os

from pybank.cbs import CBS
from pybank.db import Database 

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


class TestDatabaseInsertCardRecord(unittest.TestCase):
    def setUp(self):
        self.db_name = 'tests.db'
        self.db = Database(self.db_name)

    def tearDown(self):
        os.remove(self.db_name)

    def test_insert_valid_card_record(self):
        self.assertTrue(self.db.insert_card_record(('8930011234567890', 100500.00, 826)))

    def test_insert_invalid_card_record(self):
        self.assertFalse(self.db.insert_card_record(('8930011234567890', 100500.00)))

    def test_insert_duplicate_card_records(self):
        self.assertTrue(self.db.insert_card_record(('8930011234567890', 100500.00, 826)))
        self.assertFalse(self.db.insert_card_record(('8930011234567890', 100500.00, 826)))

    def test_insert_differenct_card_records(self):
        self.assertTrue(self.db.insert_card_record(('3333333333333333', 100500.00, 826)))
        self.assertTrue(self.db.insert_card_record(('4444444444444444', 100500.00, 826)))    
    
if __name__ == '__main__':
    unittest.main()