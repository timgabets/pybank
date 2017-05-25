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


	def get_card_record(self, card_no):
		self.conn.execute('select * from CARDS where card_no=?', card_no)
		self.conn.fetchone()


	def insert_card_record(self, card_record):
		try:
			self.conn.execute('insert into CARDS values(?,?,?)', card_record)
			self.conn.commit()
		except (sqlite3.IntegrityError,sqlite3.ProgrammingError) as e:
			print(e)
			return False

		return True



