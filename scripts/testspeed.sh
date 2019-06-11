#!/bin/bash

st="stcur"
speedtest-cli --simple | cat ${st}

echo "st is: $st"
echo $st
