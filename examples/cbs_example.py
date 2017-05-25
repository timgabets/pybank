#!/usr/bin/env python

from pybank.cbs import CBS

def show_help(name):
    """
    Show help and basic usage
    """
    print('Usage: python3 {} [OPTIONS]... '.format(name))
    print('ISO8583 Core banking system simulator')
    print('  -p, --port=[PORT]\t\tTCP port to connect to, 3388 by default')
    print('  -s, --server=[IP]\t\tIP of the host to connect to, 127.0.0.1 by default')


if __name__ == '__main__':
    ip = ''
    port = 3388

    optlist, args = getopt.getopt(sys.argv[1:], 'hp:s:', ['help', 'port=', 'server='])
    for opt, arg in optlist:
        if opt in ('-h', '--help'):
            show_help(sys.argv[0])
            sys.exit()
        elif opt in ('-p', '--port'):
            try:
                port = int(arg)
            except ValueError:
                print('Invalid TCP port: {}'.format(arg))
                sys.exit()

        elif opt in ('-s', '--server'):
            ip = arg

    cbs = CBS(host=ip, port=port)
    cbs.run()