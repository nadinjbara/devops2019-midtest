#!/bin/bash


ext=$1
dir=$2

for file in $dir* ; do

   mv $file $file$ext
   echo $file



done
