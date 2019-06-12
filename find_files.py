#!/usr/bin/python3


import sys
import os

#check the num of the args
if(len(sys.argv) != 3):
	print("you should enter 2 arguments")
	exit(1)
	
word = sys.argv[1]
dir = sys.argv[2]

#check that  dairectory is really a directory
if(os.path.isdir(dir) == False):
	print(path + "is not a directory!")
	exit(1)

#iterating over the directory

for root,dirs,files in os.walk(dir):
	for name in files:
		file = open(name)
		for line in file.readlines():
        		if(word in line):
                		print(name)
				file.close()
                                break
		file.close()
