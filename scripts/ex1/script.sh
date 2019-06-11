#!/bin/bash

echo "HEllo World"

if [[ `whoami` == "root" ]]; then
	echo good
	exit 1


fi
