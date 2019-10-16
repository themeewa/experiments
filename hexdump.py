import sys


def reshape(data, col):
	rdata=[]
	while data:
		rdata.append(data[:col])
		del data[:col]
	return rdata

filename  = sys.argv[1]
flags = sys.argv[2:]
content = open(filename).read()
# for part in content:
byte_cont = content.encode("utf-8")
byte_cont_new = [x for x in byte_cont]
reshaped = reshape(byte_cont_new, 16)
count =0
for line in reshaped:
	print(f"{count:010x}", end=" ")
	print(" ".join(f"{x:02x}" for x in line))
	count+=1
	# print(line)