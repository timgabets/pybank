import sqlite3
import random
from math import pow


class Database:
	def __init__(self, db_name=None):
		self.db_name = db_name if db_name else 'cbs.db'

		self.conn = sqlite3.connect(self.db_name)
		self.cursor = self.conn.cursor()
		try:
			self.conn.execute('select 1 from CARDS')
		except sqlite3.OperationalError:
			self.db_init()


	def db_init(self):
		self.conn = sqlite3.connect(self.db_name)
		self.cursor = self.conn.cursor()
		self.conn.execute('create table ACCOUNTS (account_number INTEGER, type INTEGER default 0, currency INTEGER, balance real, constraint ACCOUNT_CURRENCY_UK unique(account_number, currency));')
		self.conn.execute('create table CARDS (card_number INTEGER, currency INTEGER, account INTEGER, constraint CARD_CURRENCY_UK unique(card_number, currency), FOREIGN KEY(account) REFERENCES accounts(account_number));')


	def get_card_balance(self, card, currency_code):
		"""
		"""
		t = (card,currency_code)
		self.cursor.execute('select balance from ACCOUNTS where account_number=(select account from CARDS where card_number=? and currency=?)', t)
		row = self.cursor.fetchone()
		return row[0] if row else None


	def generate_account_number(self):
		"""
		"""
		return '408178101000' + str(random.randint(pow(2, 8*2), pow(2, 8*4)))


	def create_account(self, currency, balance):
		"""
		"""
		account_number = self.generate_account_number()
		# TODO: check currency exponent
		t = (account_number, currency, format(balance, '.2f'))
		try:
			self.conn.execute('insert into ACCOUNTS(account_number, currency, balance) values(?,?,?)', t)
			self.conn.commit()
		except (sqlite3.IntegrityError,sqlite3.ProgrammingError) as e:
			print(e)
			return False
		return account_number


	def insert_card_record(self, card, currency, balance):
		"""
		"""
		account_number = self.create_account(currency, balance)
		if not account_number:
			return False

		t = (card, currency, account_number)
		try:
			self.conn.execute('insert into CARDS(card_number, currency, account) values(?,?,?)', t)
			self.conn.commit()
		except (sqlite3.IntegrityError,sqlite3.ProgrammingError) as e:
			print(e)
			return False
		return True


	def update_card_balance(self, card, currency, new_balance):
		"""
		"""
		if self.card_has_account(card, currency):
			try:
				# TODO: check currency exponent
				t = (format(new_balance, '.2f'), card, currency)
				self.cursor.execute('update ACCOUNTS set balance=? where account_number=(select account from cards where card_number=? and currency=?)', t)
				self.conn.commit()
				return True
			except:
				return False
		else:
			return None


	def card_has_account(self, card, currency):
		"""
		"""
		t = (card,currency)
		self.cursor.execute('select 1 from CARDS where card_number=? and currency=?', t)
		row = self.cursor.fetchone()
		return True if row else False


	def card_exists(self, card):
		"""
		"""
		t = (card,)
		self.cursor.execute('select 1 from CARDS where card_number=?', t)
		row = self.cursor.fetchone()
		return True if row else False		
