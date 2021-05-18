from tools import *
import csv
import argparse
import sys

def error(msg):
    print(msg)
    sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Must be have a data file")
    args = parser.parse_args()
    if not getattr(args, 'file'):
        error('data.csv expected')
    x = get_data(args.file)