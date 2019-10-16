import subprocess
import sys

command = sys.argv[1:]

for line in sys.stdin.readlines():
	exec = command+[line.strip()]
	try:
		status = subprocess.run(exec)
	except :
		print("some error/exception occured")