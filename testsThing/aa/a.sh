#!/bin/bash

ext=$1
dir=$2

#echo $ext
#echo $dir

for file in $dir* ; do
   echo $file
   if [[ "$file" != "*.mp3" ]]
   then
   	mv $file $file$ext
	echo "i"
   fi
	#echo $file  
 done

