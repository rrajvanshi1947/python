if [ $# -ne 2  ]
	then
		echo Provide 2 numerical arguments
		exit 1
	fi

echo `expr $1 + $2`
