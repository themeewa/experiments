import sys

count = 1
if '-n' in sys.argv[1:]:
    for file in sys.argv[1:]:
        if file =='-n':
            continue
        else:
            lines = open(file).readlines()
            print(count+line for line in lines)
    if len(sys.argv)>1:
        for file in sys.argv[1:]:
            content = open(file).read()
            print(content)
    else:
        print("pass atleast one file to process")