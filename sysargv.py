#take command line argument and print out detailed list of all the flags passed and missed 

import sys

# print("total args passed: ")
# print(len(sys.argv))
# print("and arguments are: ")
# for x in sys.argv:
	# print(x)
	# print(" ")
if ("-h"  in sys.argv or "--help" in sys.argv):
	print("called for help messege")

if ("-v"  in sys.argv or "--version" in sys.argv):
	print("called for version")

count = len(sys.argv)


for i in range(count)[1:]:
	print(sys.argv[i])
	if sys.argv[i] == "-p" or sys.argv[i] == "--path":
		path = sys.argv[i+1]
		

if ("--verbose" in sys.argv or "-x" in sys.argv):
	verbose=True

if ("--cool" in sys.argv or "-c" in sys.argv):
	cool=True

