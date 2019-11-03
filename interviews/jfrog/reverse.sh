#!/bin/bash
var=$1
if [ $var -lt 0 ]
	then
		echo Please enter positive number
		exit 1
fi

rev=0


while [ $var -gt 0 ]
	do
		rev=`expr $rev \* 10 + $var % 10`
		var=`expr $var / 10`
	done

echo $rev
