from sets import Set

distinct_values  =  Set([])
f = open ('redis_api_host_keys_without_expiration', 'r')

for line in f: 
	if ":" in line:	
		distinct_values.add( line[0: line.index(":")])
	else: distinct_values.add( line)

print distinct_values
