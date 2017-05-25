#!/usr/bin/env python

import socket
import sys
import struct
import sqlite3

from binascii import hexlify

from bpc8583.ISO8583 import ISO8583, MemDump, ParseError
from bpc8583.spec import IsoSpec, IsoSpec1987ASCII, IsoSpec1987BPC
from bpc8583.tools import get_response
from tracetools.tracetools import trace
from pynblock.tools import B2raw

from pybank.db import Database

class CBS:
    def __init__(self, host=None, port=None):
        if host:
            self.host = host
        else:
            self.host = '127.0.0.1'

        if port:
            try:
                self.port = int(port)
            except ValueError:
                print('Invalid TCP port: {}'.format(arg))
                sys.exit()
        else:
            self.port = 3388

        self.db_name = 'cbs.db'
        self.conn = sqlite3.connect(self.db_name)
        self.db = self.conn.cursor()


    def get_message_length(self, message):
        return B2raw(bytes(str(len(message)).zfill(4), 'utf-8'))


    def get_balance_string(self, balance, currency_code):
        """
        Get balance string, according to Field 54 description
        """
        if not balance or not currency_code:
            return ''
    
        if float(balance) > 0:
            amount_sign = 'C'
        else:
            amount_sign = 'D'
    
        balance_formatted = balance.replace(' ', '').replace('.', '').replace('-', '').zfill(12)
        balance_string = amount_sign + balance_formatted + currency_code
    
        return str(len(balance_string)).zfill(3) + balance_string


    def connect(self):
        """
        """
        try:
            self.sock = None
            for res in socket.getaddrinfo(self.host, self.port, socket.AF_UNSPEC, socket.SOCK_STREAM):
                af, socktype, proto, canonname, sa = res
                self.sock = socket.socket(af, socktype, proto)
                self.sock.connect(sa)
        except OSError as msg:
            print('Error connecting to {}:{} - {}'.format(self.host, self.port, msg))
            sys.exit()
        print('Connected to {}:{}'.format(self.host, self.port))


    def process_trxn_balance_inquiry(self, response):
        account_number = str(response.FieldData(2))
        currency_code = str(response.FieldData(49))

        print(account_number)

        t = (account_number,)
        self.db.execute('select * from CARDS where card_no=?', t)
        print(self.db.fetchone())

        response.FieldData(54, '007' + self.get_balance_string('1234.56', '643'))
        response.FieldData(39, '00')


    def run(self):
        """
        """
        while True:
            try:
                self.connect()

                while True:
                    data = self.sock.recv(4096)
                    if len(data) > 0:
                        trace(title='<< {} bytes received: '.format(len(data)), data=data)
                    
                    request = ISO8583(data[2:], IsoSpec1987BPC())
                    request.Print()

                    response = ISO8583(data[2:], IsoSpec1987BPC())
                    response.MTI(get_response(request.get_MTI()))            
                    
                    processing_code = str(request.FieldData(3)).zfill(6)
                    
                    if processing_code[0:2] == '31':
                        self.process_trxn_balance_inquiry(response)
                    else:
                        response.FieldData(39, '000')
                        
                    # TODO: fix these fields:
                    response.RemoveField(9)
                    response.RemoveField(10)
                    response.RemoveField(32)
                    response.RemoveField(42)

                    response.Print()
                    
                    data = response.BuildIso()
                    data = self.get_message_length(data) + data
                    self.sock.send(data)
                    trace(title='>> {} bytes sent:'.format(len(data)), data=data)
        
            except ParseError:
                print('Connection closed')
                conn.close()

        self.sock.close()
        conn.close()
