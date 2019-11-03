for var in 0 1 2
	do
		echo $var
	done

a=5
while [ $a -lt 8  ]
	do
		echo $a
		a=`expr $a + 1`
	done

b=15
until [  $b -ge 18  ]
        do
                echo $b
                b=`expr $b + 1`
        done
