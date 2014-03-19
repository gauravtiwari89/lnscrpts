a= 123454321

def reverse(a):
	temp = 0 
	while (a!=0):
		temp = temp*10 + a%10
		a = a/10
	return temp


print reverse(a) == a 
