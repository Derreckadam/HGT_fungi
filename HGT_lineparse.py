#! /usr/bin/python
# HGT_lineparse by Derreck
import csv
import sys

hgttxt = sys.argv[1]

print ("input file: " + hgttxt)

with open(hgttxt, 'rb') as csvfile:
	reader = csv.reader(csvfile)
	count = 0
	hits = open("HGTFILE.txt", "wb")
	for row in reader:
		count += 1
		if count >= 8:
			col1 = row[0].split("  ")
			if len(col1) == 5:
				col5 = col1[4].strip("\$")
				col5 = float(col5.strip())
				print col5
				hits.write("Column No: " + str(count - 8) + "   e Value: " + str(col5) + "\n")
	print ("Here: ", count - 8)		
	hits.close()