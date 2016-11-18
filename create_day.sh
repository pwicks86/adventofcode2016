#!/bin/bash

day=$1

day_len=${#day} 

if [[ $day_len == 1 ]]
then
    dir_name=day0$1
else
    dir_name=day$1
fi

mkdir $dir_name
echo "f = open('input.txt')" > $dir_name/p1.py
echo "f = open('input.txt')" > $dir_name/p2.py

wget -O $dir_name/input.txt http://adventofcode.com/2016/$day/input
