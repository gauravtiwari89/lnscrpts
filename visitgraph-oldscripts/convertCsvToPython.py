#!/usr/bin/python

import sys, os
import simplejson, csv


inputFile = "structuredlogData.dat"
outputFile = sys.argv[1]
outdata = open(outputFile, 'a')
csvreader =  csv.reader(sys.stdin, delimiter="#")
outDict = {}
valuearray=[]
for row in csvreader:
	if len(row)== 5:	
		valuearray.append({"ip":row[0], "timestamp":row[1], "httpUrl": row[2], "ctc": row[3], "url": row[4]})

outDict["results"] = valuearray

print >>outdata, simplejson.dumps(outDict)
