#!/bin/bash

set -e

# convert all the incoming xml to csv
for xml in incoming/xml/*
do
	echo $xml
	out=`basename $xml .xml | awk -F_ '{print $NF}'`.csv
	python3 ../greenbutton_to_csv.py $xml | tee output_csv/$out | wc
	mv $xml processed/xml/`basename $xml`
done

# Combine all the CSVs into all.csv
wc all.csv output_csv/*
cat output_csv/*.csv  | sort | uniq > all.csv
wc all.csv
