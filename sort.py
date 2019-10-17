import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('input', nargs='*')
parser.add_argument('-r', action='store_true')

args = parser.parse_args()

if not args.input:
    inputs = sys.stdin.readlines()
else:
    inputs=[]
    for file in args.input:
        for line in open(file).readlines():
            open(file).readlines()
            inputs.append(line)
sortedcont = sorted([line for line in inputs], reverse = args.r )
for line in sortedcont:
    print(line)