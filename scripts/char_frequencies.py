#!/usr/bin/python3

import sys
import os

if(len(sys.argv) != 2):
	print("Illegal number of arguments!")
	exit(1)

my_string = sys.argv[1]
freq_dict = dict()


for c in my_string:
	if(c in freq_dict):
		freq_dict[c] += 1

	else:
		freq_dict[c] = 1

print(freq_dict)
