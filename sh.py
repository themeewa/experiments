import sys, os
import subprocess
import pdb

# def shell():
# 	# comm = "clear"
# 	comm = sys.stdin.readline().strip()
# 	print(comm)
# 	status = subprocess.run(comm)
# 	print(status.returncode)
# 	# if status.returncode == 0:
# 	shell()
# shell()
def interpret(exec):
	if exec[0]=='exit':
		sys.exit(0)
	elif exec[0] == 'cd':
		if len(exec)==2:
			os.chdir(exec[1])
		else:
			print("error: ch DIR")
	else:
		try:
			subprocess.run(exec)
		except :
			print("error occured: ")
			return 1

def parse(line):
	return [x.strip() for x in line.split(' ') if x]

def run(comm):
	exec = parse(comm)
	# print(exec)
	# return 0
	pdb.set_trace()
	if exec:
		return interpret(exec)
	return None

def main():
	while True:	
		try:
			# line = input('>  ')
			line = "pwd"

			status = run(line)
		except KeyboardInterrupt:
			sys.exit(0)

main()