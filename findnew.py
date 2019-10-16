from pathlib import Path
import sys
import argparse

def name_find(dpath,args):
	print("name find called")
	for f in dpath.rglob(args.name):
		if args.print:
			# print(str(f)+"~~~~~~~")
			print(open(f).read())
		else:
			print(f)
def type_find(dpath, args):
	print("type find called")
	for f in dpath.rglob(args.name):
		if args.type=='f' and f.is_file():
			if args.print:
				# print(str(f)+"~~~~~~~")
				print(open(f).read())
			else:
				print(f)
		elif args.type=='d' and f.is_dir():
			print(f)

parser = argparse.ArgumentParser()
parser.add_argument('start', nargs=1, type=str)
parser.add_argument('--name', type=str)
parser.add_argument('--type', type=str, choices = ['d','f'])
parser.add_argument('--print', action = 'store_true')
parser.add_argument('--exec', action = 'store_true')

args = parser.parse_args()

dirpath = Path(args.start[0])

if args.name and not args.type:
	name_find(dirpath, args)
else:
	type_find(dirpath, args)

print(args)