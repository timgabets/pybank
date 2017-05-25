import sqlite3

class Database:
	def __init__(self, db_name=None):
		if db_name:
			self.db_name = db_name
		else:
			self.db_name = 'cbs.db'

		self.conn = sqlite3.connect(self.db_name)
		self.cursor = self.conn.cursor()
		try:
			self.conn.execute('select 1 from CARDS')
		except sqlite3.OperationalError:
			self.db_init()


	def db_init(self):
		self.conn = sqlite3.connect(self.db_name)
		self.cursor = self.conn.cursor()
		self.conn.execute('create table CARDS (card_no text, currency text, balance real, constraint CARD_CURRENCY_UK unique(card_no, currency))')


	def get_card_balance(self, card, currency_code):
		"""
		"""
		t = (card,currency_code)
		self.cursor.execute('select balance from CARDS where card_no=? and currency=?', t)
		row = self.cursor.fetchone()
		if row:
			return row[0]
		else:
			return None

	def insert_card_record(self, card_record):
		"""
		card_record is a tuple, containing neede values, e.g. ('2006-03-28', 'BUY', 'IBM', 1000, 45.00)
		"""
		try:
			self.conn.execute('insert into CARDS values(?,?,?)', card_record)
			self.conn.commit()
		except (sqlite3.IntegrityError,sqlite3.ProgrammingError) as e:
			print(e)
			return False
		return True


	def update_card_balance(self, card, currency, new_balance):
		"""
		"""
		if self.account_exists(card, currency):
			try:
				t = (new_balance, card, currency)
				self.cursor.execute('update CARDS set balance=? where card_no=? and currency=?', t)
				self.conn.commit()
				return True
			except:
				return False
		else:
			return None


	def account_exists(self, card, currency):
		"""
		"""
		t = (card,currency)
		self.cursor.execute('select 1 from CARDS where card_no=? and currency=?', t)
		row = self.cursor.fetchone()
		if row:
			return True
		else:
			return False



