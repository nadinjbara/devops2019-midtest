#!/usr/bin/python3

import sys
import os
from pathlib import Path
import hashlib
import multiprocessing
import time


if(len(sys.argv) != 2):
	print("Illegal number of arguments!")
	exit(1)

dir = sys.argv[1]

if(os.path.isdir(dir) == False):
	print(dir + " is not a directory")
	exit(1)


def worker(lock, name, cnt):

	print(str(cnt) +  "./" + name + "," + hashlib.md5(name.encode('utf-8')).hexdigest())

if __name__ == '__main__':
	
	counter_lock = multiprocessing.Lock()
	
	count = 1
	for root,dirs,files in os.walk(dir):
		for name in files:		
			if(name.endswith(".csv")):
				p = multiprocessing.Process(target = worker, args = (counter_lock,name,count,))
				count += 1
				p.start()
				p.join()



