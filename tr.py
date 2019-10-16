import sys

args = sys.argv[1:]
instr = sys.stdin.read()
print(instr)
print(args)

if args[0]== '-t':
	fromc = int(args[1])
	toc = int(args[2])
	outstr = instr[fromc:toc]
	print(outstr)
else:
	fromc=args[0]
	toc=args[1]
	print(instr.replace(fromc, toc))
