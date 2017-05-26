pybank
=======

A python library that implements the primitive Core Banking system (CBS) emulator.

Usage:
 >>> from pybank.cbs import CBS
 >>> #A host to connect to
 >>> cbs = CBS(host='127.0.0.1', port=3388)
 >>> cbs.run()
 Connected to 127.0.0.1:3388
	Parsed message:
	MTI:    [1804]
	Fields: [ 11 12 24 ]
		 11 - System trace audit number                 [661281]
		 12 - Time, local transaction (YYMMDDhhmmss)    [170526181337]
		 24 - Network International identifier (NII)    [801]
 18:13:37.868027 >> 35 bytes sent:
	00 33 31 38 30 34 00 30 01 00 00 00 00 00 36 36         .31804.0......66
	31 32 38 31 31 37 30 35 32 36 31 38 31 33 33 37         1281170526181337
	38 30 31                                                801
 18:13:37.903578 << 26 bytes received: 
	00 24 31 38 31 34 00 20 01 00 02 00 00 00 30 30         .$1814. ......00
	30 30 30 30 38 30 31 30 30 30                           0000801000
	Parsed message:
	MTI:    [1814]
	Fields: [ 11 24 39 ]
		 11 - System trace audit number                 [000000]
		 24 - Network International identifier (NII)    [801]
		 39 - Response code                             [000]			[APPROVED]
 18:13:41.778900 << 272 bytes received: 
	02 70 31 31 30 30 f4 b6 40 01 08 e1 e4 00 00 00         .p1100..@.......
	00 00 14 00 00 00 31 36 34 31 37 34 30 37 30 30         ......1641740700
	30 30 30 30 30 31 30 34 33 31 30 30 30 30 30 30         0000010431000000
	30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30         0000000000000000
	30 30 30 30 30 30 30 30 30 30 30 30 30 30 31 31         0000000000000011
	33 30 35 33 30 35 32 36 30 31 31 38 31 33 34 31         3053052601181341
	31 37 31 32 30 32 30 32 32 38 36 30 31 30 30 36         1712020228601006
	30 30 30 30 30 30 30 30 30 30 30 30 31 31 33 30         0000000000001130
	35 33 31 30 30 30 31 33 33 37 39 39 39 39 39 39         5310001337999999
	39 39 39 39 39 39 30 30 31 42 50 43 20 54 45 53         999999001BPC TES
	54 20 4d 45 52 43 48 41 4e 54 20 4e 20 31 3e 4d         T MERCHANT N 1>M
	4f 53 4b 56 41 20 20 20 20 20 20 20 20 20 20 52         OSKVA          R
	55 30 34 37 30 30 31 30 30 31 31 30 30 32 30 30         U047001001100200
	33 37 30 32 30 32 35 30 30 31 32 30 32 37 30 30         3702025001202700
	30 30 32 38 30 31 32 30 30 30 30 30 30 31 31 33         0028012000000113
	30 35 33 36 34 33 38 32 36 38 32 36 30 30 30 30         0536438268260000
	30 30 31 31 31 39 35 36 37 31 33 30 30 30 30 31         0011195671300001
	Parsed message:
	MTI:    [1100]
	Fields: [ 2 3 4 6 9 11 12 14 15 18 32 37 41 42 43 48 49 50 51 54 100 102 ]
		  2 - Primary account number (PAN)              [4174070000000104]
		  3 - Processing code                           [310000]
		  4 - Amount, transaction                       [000000000000]
		  6 - Amount, cardholder billing                [000000000000]
		  9 - Conversion rate, settlement               [00000000]
		 11 - System trace audit number                 [113053]
		 12 - Time, local transaction (YYMMDDhhmmss)    [052601181341]
		 14 - Date, expiration                          [1712]
		 15 - Date, settlement                          [020228]
		 18 - Merchant type                             [6010]
		 32 - Acquiring institution identification code [0]
		 37 - Retrieval reference number                [000000113053]
		 41 - Terminal ID                               [10001337]
		 42 - Merchant number                           [999999999999001]
		 43 - Card acceptor name/location               [BPC TEST MERCHANT N 1>MOSKVA          RU]
		 48 - Additional data - private                 [00100110020037020250012027000028012000000113053]
		 49 - Currency code, transaction                [643]
		 50 - Currency code, settlement                 [826]
		 51 - Currency code, cardholder billing         [826]
		 54 - Additional amounts                        []
		100 - Receiving institution identification code []
		102 - Account identification 1                  [1]
	Parsed message:
	MTI:    [1110]
	Fields: [ 2 3 4 6 11 12 14 15 32 37 39 48 49 50 51 54 102 ]
		  2 - Primary account number (PAN)              [4174070000000104]
		  3 - Processing code                           [310000]
		  4 - Amount, transaction                       [000000000000]
		  6 - Amount, cardholder billing                [000000000000]
		 11 - System trace audit number                 [113053]
		 12 - Time, local transaction (YYMMDDhhmmss)    [052601181341]
		 14 - Date, expiration                          [1712]
		 15 - Date, settlement                          [020228]
		 32 - Acquiring institution identification code [0]
		 37 - Retrieval reference number                [000000113053]
		 39 - Response code                             [000]			[APPROVED]
		 48 - Additional data - private                 [00100110020037020250012027000028012000000113053]
		 49 - Currency code, transaction                [643]
		 50 - Currency code, settlement                 [826]
		 51 - Currency code, cardholder billing         [826]
		 54 - Additional amounts                        [007016C000000135502826]
		102 - Account identification 1                  [1]
 18:13:41.787069 >> 203 bytes sent:
	02 01 31 31 31 30 f4 36 00 01 0a 01 e4 00 00 00         ..1110.6........
	00 00 04 00 00 00 31 36 34 31 37 34 30 37 30 30         ......1641740700
	30 30 30 30 30 31 30 34 33 31 30 30 30 30 30 30         0000010431000000
	30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30         0000000000000000
	30 30 30 30 30 30 31 31 33 30 35 33 30 35 32 36         0000001130530526
	30 31 31 38 31 33 34 31 31 37 31 32 30 32 30 32         0118134117120202
	32 38 30 31 30 30 30 30 30 30 30 31 31 33 30 35         2801000000011305
	33 30 30 30 30 34 37 30 30 31 30 30 31 31 30 30         3000047001001100
	32 30 30 33 37 30 32 30 32 35 30 30 31 32 30 32         2003702025001202
	37 30 30 30 30 32 38 30 31 32 30 30 30 30 30 30         7000028012000000
	31 31 33 30 35 33 36 34 33 38 32 36 38 32 36 30         1130536438268260
	32 32 30 30 37 30 31 36 43 30 30 30 30 30 30 31         22007016C0000001
	33 35 35 30 32 38 32 36 30 31 31                        35502826011

cbs_example.py_ is an example of core banking system emulator application, that interacts connects to authorization switch through ISO8583:1993 protocol (accounts, transactions and balances are stored in a local sqlite3 database).

.. _cbs_example.py: https://github.com/timgabets/pybank/tree/master/examples/cbs_example.py
