#!/usr/bin/python3

#The script gets a directory and prints md5s of the files inside it using multiprocessing pool
#another version of rec_mp_ls.py

import glob
import sys
import os
import hashlib
import multiprocessing
from multiprocessing import pool 

#check usage

if(len(sys.argv) != 2):
	print("Wrong usage")
	exit(1)

#check arg is a directory

dir = sys.argv[1]
if(not os.path.isdir(dir)):
	print(dir, "is not a directory")

#Define worker function to perform a given job

def worker(job):
	(num,file) = job
	print(str(num)+","+str(file)+","+hashlib.md5(open(file,'rb').read()).hexdigest())
	return

#create worksheet - array of pairs, each pair will be (serial_num, file_to_work_on)

i = 0
worksheet = []
for root, dirnames,filenames in os.walk(dir):
	for filename in filenames:
		i += 1
		filename = os.path.join(root, filename)
		worksheet.append((i,filename))

#create work pool and divide work between processors

p = Pool(multiprocessing.cpu_count())
p.map(worker,worksheet)























	

















