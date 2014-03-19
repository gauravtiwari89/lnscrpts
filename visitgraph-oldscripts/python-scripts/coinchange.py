#!/usr/bin/python

coins=[1, 2, 5, 10]
val =50
start = 0

def denominate(x, count):	
	if x<=0:
		return count
	temp=[]
	for coin in coins:
		temp.append(denominate(x-coin, count+1))
	return min(temp)	

print denominate(val, start)	
