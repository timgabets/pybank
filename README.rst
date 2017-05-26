pybank
=======

A python library that implements the primitive Core Banking system (CBS) emulator.

Usage:
 >>> from pybank.cbs import CBS
 >>> cbs = CBS(host=ip, port=port)
 >>> cbs.run()

cbs_example.py_ is an example of core banking system emulator application, that interacts connects to authorization switch through ISO8583:1993 protocol (accounts, transactions and balances are stored in a local sqlite3 database).

.. _cbs_example.py: https://github.com/timgabets/pybank/tree/master/examples/cbs_example.py
