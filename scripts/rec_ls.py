#!/usr/bin/python3

import sys
import os
from pathlib import Path
import hashlib


if(len(sys.argv) != 2):
	print("Illegal number of arguments!")
	exit(1)

dir = sys.argv[1]

if(os.path.isdir(dir) == False):
	print(dir + "is not a directory")
	exit(1)
cnt = 1

for root,dirs,files in os.walk(dir):
	for name in files:
		if(name.endswith(".csv")):
			print(str(cnt) +  "./" + name + "," + hashlib.md5(name.encode('utf-8')).hexdigest())
			cnt += 1 				
