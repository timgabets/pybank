#!/usr/bin/env python

import unittest
import os

from pybank.cbs import CBS
from pybank.db import Database 

class TestGetFloatAmount(unittest.TestCase):
    def setUp(self):
        self.cbs = CBS(host=None, port=None)

    def test_get_float_amount(self):
       self.assertEqual(self.cbs.get_float_amount(3585, 643), 35.85)

    def test_get_float_amount_large(self):
       self.assertEqual(self.cbs.get_float_amount(999999999999, 643), 9999999999.99)

    def test_get_float_amount_small(self):
       self.assertEqual(self.cbs.get_float_amount(13, 643), 0.13)


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
        self.assertEqual(self.cbs.get_balance_string(1234.56, '643'), '007016C000000123456643')

    def test_get_balance_string_positive_no_decimals(self):
        self.assertEqual(self.cbs.get_balance_string(1234, '643'), '007016C000000123400643')

    def test_get_balance_string_negative(self):
        self.assertEqual(self.cbs.get_balance_string(-1234.59, '826'), '007016D000000123459826')


class TestDatabaseInsertCardRecord(unittest.TestCase):
    def setUp(self):
        self.db_name = 'tests.db'
        self.db = Database(self.db_name)

    def tearDown(self):
        os.remove(self.db_name)

    def test_insert_valid_card_record(self):
        self.assertTrue(self.db.insert_card_record('8930011234567890', 826, 100500.00))

    def test_insert_duplicate_card_records(self):
        self.assertTrue(self.db.insert_card_record('8930011234567890', 826, 100500.00))
        self.assertFalse(self.db.insert_card_record('8930011234567890', 826, 100500.00))

    def test_insert_differenct_card_records(self):
        self.assertTrue(self.db.insert_card_record('3333333333333333', 826, 100500.00))
        self.assertTrue(self.db.insert_card_record('4444444444444444', 826, 100500.00))    
   
    def test_insert_valid_card_record_check_precision(self):
        self.assertTrue(self.db.insert_card_record('8930011234567890', 826, 100500.00000007))
        self.assertEqual(self.db.get_card_balance('8930011234567890', 826), 100500.0)


class TestDatabaseGetCardBalance(unittest.TestCase):
    def setUp(self):
        self.db_name = 'tests.db'
        self.db = Database(self.db_name)
        self.card = '8930011234567890'
        self.currency = 826
        self.db.insert_card_record(self.card, self.currency, 100500.00)

    def tearDown(self):
        os.remove(self.db_name)

    def test_get_card_balance_valid_card(self):
        self.assertEqual(self.db.get_card_balance(self.card, self.currency), 100500.0)

    def test_get_card_balance_currecy_as_string(self):
        self.assertEqual(self.db.get_card_balance(self.card, '826'), 100500.0)

    def test_get_card_balance_wrong_currency(self):
        self.assertEqual(self.db.get_card_balance(self.card, 840), None)

    def test_get_card_balance_inexistent_card(self):
        self.assertEqual(self.db.get_card_balance('801803291823', self.currency), None)

    def test_get_card_balance_card_no_empty(self):
        self.assertEqual(self.db.get_card_balance('', self.currency), None)


class TestDatabaseCardHasAccount(unittest.TestCase):
    def setUp(self):
        self.db_name = 'tests.db'
        self.db = Database(self.db_name)
        self.card = '8930011234567890'
        self.currency = 826
        self.db.insert_card_record(self.card, self.currency, 100500.00)

    def tearDown(self):
        os.remove(self.db_name)

    def test_card_has_account(self):
        self.assertTrue(self.db.card_has_account(self.card, self.currency))

    def test_account_doesnt_exists_wrong_card(self):
        self.assertFalse(self.db.card_has_account('192830918039', self.currency))
    
    def test_account_doesnt_exists_wrong_currency(self):
        self.assertFalse(self.db.card_has_account(self.card, 643))


class TestDatabaseCardExists(unittest.TestCase):
    def setUp(self):
        self.db_name = 'tests.db'
        self.db = Database(self.db_name)
        self.card = '8930011234567890'
    
    def tearDown(self):
        os.remove(self.db_name)

    def test_card_does_not_exist(self):
        self.assertFalse(self.db.card_exists(self.card))

    def test_card_exists(self):
        self.db.insert_card_record(self.card, 643, 100500.00)
        self.assertTrue(self.db.card_exists(self.card))


class TestDatabaseUpdateCardBalance(unittest.TestCase):
    def setUp(self):
        self.db_name = 'tests.db'
        self.db = Database(self.db_name)
        self.card = '8930011234567890'
        self.currency = 826
        self.db.insert_card_record(self.card, self.currency, 100500.00)

    def tearDown(self):
        os.remove(self.db_name)

    def test_update_card_balance(self):
        new_balance = 12.34
        self.assertTrue(self.db.update_card_balance(self.card, self.currency, new_balance))
        self.assertEqual(self.db.get_card_balance(self.card, self.currency), new_balance)

    def test_update_card_balance_wrong_card(self):
        new_balance = 12.34
        self.assertEqual(self.db.update_card_balance('iddqd', self.currency, new_balance), None)

    def test_update_card_balance_wrong_currency(self):
        new_balance = 12.34
        self.assertEqual(self.db.update_card_balance(self.card, 840, new_balance), None)
        self.assertEqual(self.db.get_card_balance(self.card, 840), None)

    def test_update_card_balance_check_precision(self):
        new_balance = 17.890000000003
        self.assertTrue(self.db.update_card_balance(self.card, 826, new_balance))
        self.assertEqual(self.db.get_card_balance(self.card, 826), 17.89)


class TestDatabaseInsertTransactionRecord(unittest.TestCase):
    def setUp(self):
        self.db_name = 'tests.db'
        self.db = Database(self.db_name)
        self.db.insert_card_record('8930011234567890', 826, 100500.00)

    def tearDown(self):
        os.remove(self.db_name)

    def test_insert_valid_transaction_record(self):
        self.db.insert_transaction_record('1110', '8930011234567890', 826, 30.0, prcode=None);
        
        last_trxns = self.db.get_last_transactions('8930011234567890')
        last_trxn = last_trxns[0]
        self.assertEqual(last_trxn[0], 30.0 )
    """
    def test_insert_valid_transaction_record_with_prcode(self):
        self.db.insert_transaction_record('8930011234567890', 826, 23.12, '010000');
        
        last_trxns = self.db.get_last_transactions('8930011234567890')
        last_trxn = last_trxns[0]
        self.assertEqual(last_trxn[0], 23.12 )
        self.assertEqual(last_trxn[1], '010000' )
    """
    def test_get_three_last_transactions(self):
        self.db.insert_transaction_record('1110', '8930011234567890', 826, 23.12, '010000');
        self.db.insert_transaction_record('1420', '8930011234567890', 826, 223.44);
        self.db.insert_transaction_record('1110', '8930011234567890', 826, 19.04, '000000');
        
        last_trxns = self.db.get_last_transactions('8930011234567890', 3)
        first = last_trxns[0]
        second = last_trxns[1]
        third = last_trxns[2]

        self.assertEqual(first[0], 19.04 )
        self.assertEqual(first[1], '000000' )

        self.assertEqual(second[0], 223.44 )
        self.assertEqual(second[1], None )

        self.assertEqual(third[0], 23.12 )
        self.assertEqual(third[1], '010000' )
"""
"""

if __name__ == '__main__':
    unittest.main()