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
 18:22:45.630814 << 292 bytes received: 
	02 90 31 31 30 30 fc f6 40 01 08 e1 e4 00 00 00         ..1100..@.......
	00 00 14 00 00 00 31 36 34 31 37 34 30 37 30 30         ......1641740700
	30 30 30 30 30 31 30 34 30 30 30 30 30 30 30 30         0000010400000000
	30 30 30 30 30 31 31 30 30 30 30 30 30 30 30 30         0000011000000000
	30 30 30 31 34 39 30 30 30 30 30 30 30 30 30 31         0001490000000001
	34 39 37 30 31 33 35 31 30 30 36 31 30 30 30 30         4970135100610000
	30 30 31 31 33 30 36 30 31 37 30 35 32 36 31 38         0011306017052618
	32 32 34 35 31 37 31 32 30 32 30 32 32 38 36 30         2245171202022860
	31 30 30 36 30 30 30 30 30 30 30 30 30 30 30 30         1006000000000000
	31 31 33 30 36 30 31 30 30 30 31 33 33 37 39 39         1130601000133799
	39 39 39 39 39 39 39 39 39 39 30 30 31 42 50 43         9999999999001BPC
	20 54 45 53 54 20 4d 45 52 43 48 41 4e 54 20 4e          TEST MERCHANT N
	20 31 3e 4d 4f 53 4b 56 41 20 20 20 20 20 20 20          1>MOSKVA       
	20 20 20 52 55 30 34 37 30 30 31 30 30 31 31 30            RU04700100110
	30 32 30 30 33 37 37 34 30 32 35 30 30 31 32 30         0200377402500120
	32 37 30 30 30 30 32 38 30 31 32 30 30 30 30 30         2700002801200000
	30 31 31 33 30 36 30 36 34 33 38 32 36 38 32 36         0113060643826826
	30 30 30 30 30 30 31 31 31 39 35 36 37 31 33 30         0000001119567130
	30 30 30 31                                             0001
	Parsed message:
	MTI:    [1100]
	Fields: [ 2 3 4 5 6 9 10 11 12 14 15 18 32 37 41 42 43 48 49 50 51 54 100 102 ]
		  2 - Primary account number (PAN)              [4174070000000104]
		  3 - Processing code                           [000000]
		  4 - Amount, transaction                       [000000011000]
		  5 - Amount, settlement                        [000000000149]
		  6 - Amount, cardholder billing                [000000000149]
		  9 - Conversion rate, settlement               [70135100]
		 10 - Conversion rate, cardholder billing       [61000000]
		 11 - System trace audit number                 [113060]
		 12 - Time, local transaction (YYMMDDhhmmss)    [170526182245]
		 14 - Date, expiration                          [1712]
		 15 - Date, settlement                          [020228]
		 18 - Merchant type                             [6010]
		 32 - Acquiring institution identification code [0]
		 37 - Retrieval reference number                [000000113060]
		 41 - Terminal ID                               [10001337]
		 42 - Merchant number                           [999999999999001]
		 43 - Card acceptor name/location               [BPC TEST MERCHANT N 1>MOSKVA          RU]
		 48 - Additional data - private                 [00100110020037740250012027000028012000000113060]
		 49 - Currency code, transaction                [643]
		 50 - Currency code, settlement                 [826]
		 51 - Currency code, cardholder billing         [826]
		 54 - Additional amounts                        []
		100 - Receiving institution identification code []
		102 - Account identification 1                  [1]
	Parsed message:
	MTI:    [1110]
	Fields: [ 2 3 4 5 6 11 12 14 15 32 37 39 48 49 50 51 54 102 ]
		  2 - Primary account number (PAN)              [4174070000000104]
		  3 - Processing code                           [000000]
		  4 - Amount, transaction                       [000000011000]
		  5 - Amount, settlement                        [000000000149]
		  6 - Amount, cardholder billing                [000000000149]
		 11 - System trace audit number                 [113060]
		 12 - Time, local transaction (YYMMDDhhmmss)    [170526182245]
		 14 - Date, expiration                          [1712]
		 15 - Date, settlement                          [020228]
		 32 - Acquiring institution identification code [0]
		 37 - Retrieval reference number                [000000113060]
		 39 - Response code                             [000]			[APPROVED]
		 48 - Additional data - private                 [00100110020037740250012027000028012000000113060]
		 49 - Currency code, transaction                [643]
		 50 - Currency code, settlement                 [826]
		 51 - Currency code, cardholder billing         [826]
		 54 - Additional amounts                        [007016C000000135353826]
		102 - Account identification 1                  [1]
 18:22:45.666351 >> 215 bytes sent:
	02 13 31 31 31 30 fc 36 00 01 0a 01 e4 00 00 00         ..1110.6........
	00 00 04 00 00 00 31 36 34 31 37 34 30 37 30 30         ......1641740700
	30 30 30 30 30 31 30 34 30 30 30 30 30 30 30 30         0000010400000000
	30 30 30 30 30 31 31 30 30 30 30 30 30 30 30 30         0000011000000000
	30 30 30 31 34 39 30 30 30 30 30 30 30 30 30 31         0001490000000001
	34 39 31 31 33 30 36 30 31 37 30 35 32 36 31 38         4911306017052618
	32 32 34 35 31 37 31 32 30 32 30 32 32 38 30 31         2245171202022801
	30 30 30 30 30 30 30 31 31 33 30 36 30 30 30 30         0000000113060000
	30 34 37 30 30 31 30 30 31 31 30 30 32 30 30 33         0470010011002003
	37 37 34 30 32 35 30 30 31 32 30 32 37 30 30 30         7740250012027000
	30 32 38 30 31 32 30 30 30 30 30 30 31 31 33 30         0280120000001130
	36 30 36 34 33 38 32 36 38 32 36 30 32 32 30 30         6064382682602200
	37 30 31 36 43 30 30 30 30 30 30 31 33 35 33 35         7016C00000013535
	33 38 32 36 30 31 31                                    3826011
	


cbs_example.py_ is an example of core banking system emulator application, that interacts connects to authorization switch through ISO8583:1993 protocol (accounts, transactions and balances are stored in a local sqlite3 database).

.. _cbs_example.py: https://github.com/timgabets/pybank/tree/master/examples/cbs_example.py
