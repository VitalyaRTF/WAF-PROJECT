#!/bin/bash
chislo=12
for ((i=0;i<20;i++))
do
number=$RANDOM
let "number %= $chislo"
echo $number
python $number.py
sleep 1s
done
