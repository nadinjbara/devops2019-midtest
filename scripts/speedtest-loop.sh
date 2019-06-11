#!/bin/bash


if [ "$#" -ne 2 ]; then
	echo "bad input"
	exit
fi

count=$1
interval=$2

if [ "$count" -lt 0 ] || [ $interval -lt 0 ]
then
	echo "bad input"
	exit
fi

echo "#date,time,download,upload" > speedtest.csv
 
if [[ $count>0 ]]; then

	for ((i=0;i<count;i++)); do

		speed_Out=$(speedtest-cli --simple)
		Download=$(echo "$speed_Out" | grep Download | awk '{print $2}')
		Upload=$(echo "$speed_Out" | grep Upload | awk '{print $2}')
		date=$(date "+%m.%d.%y,%H:%M:%S")

		echo "${date},${Download},${Upload}" >> "speedtest.csv"	

		sleep $interval
	done
	exit
fi

if [[ $count==0 ]]; then
	while :
	do
		speed_Out=$(speedtest-cli --simple)
		Download=$(echo "$speed_Out" | grep Download | awk '{print $2}')
		Upload=$(echo "$speed_Out" | grep Upload | awk '{print $2}')
		date=$(date "+%m.%d.%y,%H:%M:%S")
		echo "${date},${Download},${Upload}" >> "speedtest.csv"	

		sleep $interval
	done
fi

