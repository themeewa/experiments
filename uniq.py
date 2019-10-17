import sys

import sys
args = sys.argv[1:]
if args[0]=='-f':
    inlines = open(args[1]).readlines()
    inlines = [line.split() for line in inlines if len(line)>2]
else:
    inlines = sys.stdin.readlines()
    inlines = [line.split() for line in inlines if len(line) > 2]
# for line in inlines:
#     s.add(line)

finlines=[]
begin=False
prev = ''
for line in inlines:
    if begin:
        if line!=prev:
            finlines.append(line)
            prev = line
    else:
        begin=True
        finlines.append(line)
        prev = line
# print(finlines)
for l in finlines:
    print(str(l))