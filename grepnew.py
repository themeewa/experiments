from pathlib import Path
import sys
import argparse
import re

parser = argparse.ArgumentParser()

parser.add_argument('pattern', type=str, nargs=1)
parser.add_argument('filepath', type=str, nargs=1)
args = parser.parse_args()

# getting all file content
regx = str(args.pattern[0])
if Path(args.filepath[0]).is_dir():
	files = Path(args.filepath[0]).rglob('*.*')
else:
	files = Path().rglob(args.filepath[0])
# print([x for x in Path(args.filepath[0]).rglob(args.filepath[0])])
# files = Path(args.filepath[0]).rglob(args.filepath[0])
# for file in files:
# 	print(file)
for file in files:
	content = open(file).readlines()
	# print(content)
	for line in content:
		# print('jkhkhjk')
		# print(line)	
		for match in re.findall(str(regx),line):
			print(str(file)+" "+line)
# files = Path(args.filepath[0]).rglob(args)