#!/usr/bin/python
a= [1, 2, 4, 6, -3, -17, 34, -4 , 66, 1, 88,-500, 90, 2 , -11, -9, 12, 45, 123, -112, 33]
maxsum=0
currsum = 0
for i in range(len((a))):
	currsum = max(maxsum + a[i], 0)
	maxsum=max(maxsum, currsum)
print maxsum
