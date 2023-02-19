from __future__ import print_function
from datetime import datetime

import os
import sys
import struct
import csv
import socket

HOST = str(sys.argv[1])
PORT = int(sys.argv[2])


def main():
    sock = socket.socket()
    sock.connect((HOST, PORT))
    datafile = '/app/data/data.csv'
    os.makedirs(os.path.dirname(datafile), exist_ok=True)
    with open(datafile, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['timestamp', 'ticker', 'price', 'size'])
        while True:
            binary_data = sock.recv(1024)
            data = unpack_data(binary_data)
            timestamp, ticker, price, size = convert_data(data)
            print("%s: %s %.2f %d" % (datetime.utcfromtimestamp(timestamp / 1000), ticker, price, size), end='')
            writer.writerow([timestamp, ticker, price, size])
            csvfile.flush()
            print(' -> SAVED')

def unpack_data(data):
    fmt = "!H Q H {}s d I"
    ticker_fmt = "b"
    ticker_len = int(struct.unpack(ticker_fmt, data[11:12])[0])
    return struct.unpack(fmt.format(ticker_len), data)


def convert_data(data):
    return data[1], data[3].decode('utf-8'), data[4], data[5]


if __name__ == '__main__':
    main()
