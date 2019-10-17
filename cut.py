import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-d', type=str)
parser.add_argument('-f', type=int, nargs=2)
parser.add_argument('files', nargs='*')
args = parser.parse_args()
if not args.files:
    content = sys.stdin.readlines()
    for line in content:
        print(str(line.split(args.d)[args.f[0]:args.f[1]]))
else:
    if args.d:
        for file in args.files:
            content = open(file).readlines()
            for line in content:
                print(str(line.split(args.d)[args.f[0]:args.f[1]]))