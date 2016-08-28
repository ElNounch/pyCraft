while [ true ]
do
	python run.py
	if [ -e "stop.txt" ]
	then
		rm "stop.txt"
		echo "Server crashed?"
		break
	fi
done
