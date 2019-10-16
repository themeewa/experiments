import argparse

parser = argparse.ArgumentParser()

parser.add_argument('files', metavar = 'F', type=str, nargs = '+', help = 'pass files to be read and printed or concatenated')
parser.add_argument('-n', action = 'store_true', help = 'if enabled, print line number for each line')

args = parser.parse_args()
linenum = 1
for filename in args.files:
	filetext = open(filename)
	if args.n:
		for line in filetext.readlines():
			print("{} {} ".format(linenum, line))
			linenum+=1
	else:
		print(filetext.read())