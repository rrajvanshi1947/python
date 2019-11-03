dir=$1

if [ -d $dir ]
	then
		echo Exists
		exit 1
	fi

echo Doesn't
