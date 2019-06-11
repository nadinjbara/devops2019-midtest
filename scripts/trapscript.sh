#!/bin/bash

trap "echo Booh!" SIGINT SIGNTERM
echo "pid is $$"

while true:
do
sleep 60
done

