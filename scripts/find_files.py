#!/usr/bin/python3

import sys
import os

if(len(sys.argv) != 3):
	print("wrong usage")
	exit(1)

my_dir = sys.argv[[1]
my_word = sys.argv[2]


if(os.path.isdir(my_dir) == False):
	print(path + "is not a dir")
	exit(1)


for root,dirs,files in os.walk(my_dir):
	for name in files:
		file = open(name)
		for line in file.readlines():
			if(my_word in line):
				print(name)
				file.close()
				break
		file.close()
























