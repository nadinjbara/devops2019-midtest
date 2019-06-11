#!/bin/bash

ext=$1
dir=$2

if [ "$#" -ne 2 ]; then
	echo "Illegal number of parameters"
fi

if [[ ! -d $2 ]]; then
	echo "$1 should be a directory"
	exit
fi

for file in $dir* ; do
	
	basename=${file##*/}
	
	if [[ $basename == *.* ]] #there is at least one dot in the file's name
	then
		base="${file%.*}" #the file's name without the last dot
		mv "$file" "$base$ext" 
	else
		mv "$file" "$file$ext"	
	fi
done


