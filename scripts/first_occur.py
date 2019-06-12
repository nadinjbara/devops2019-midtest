#!/usr/bin/python3

import sys
import os

if(len(sys.argv) != 2):
	print("wrong usage")
	exit(1)

my_str = sys.argv[1]
freq_dict = dict()
indx = 0

for c in my_str:
	if(c in freq_dict):
		indx += 1
	else:
		freq_dict[c] = indx
		indx += 1

print(freq_dict)

