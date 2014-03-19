#!/usr/bin/python

import sys, base64, re
import json, collections


pattern=	r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*\[(.*)\].*\"((GET|POST)\s([a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+).*CBS_CTC=(.*)'					
patternUrl= 	r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)'
urlbeg = r'http[s]?://?www.cbs.com(\/.*)'   
extract = r'.*/video/([a-z0-9A-Z_]+)/'


regx = re.compile(pattern) 
urlRegx= re.compile(patternUrl)
urlBegReg = re.compile(urlbeg)
extractreg = re.compile(extract)

def decodePayload(payload):
        return base64.b64decode(payload)


def processCTC(ctc):
        #only returning uuid till the log structure is more robust.     
        return ctc.split('|')[0]



def checkValidity(url):

	matchextractreg=re.search(extractreg, url)
	if matchextractreg == None:
		return None
	else :
		return matchextractreg.group(1)

def main():
	if len(sys.argv) < 2:
		print "no file as input"	
		sys.exit(0)

	logPath=sys.argv[1]

	for line in open(logPath, 'r'):			
		try:
			match = re.search(regx, line)
			ip= match.group(1)
			timestamp= match.group(2)
			getUrl= match.group(3)
			ctc = match.group(6)
			matchurl = re.search(urlRegx, line)				
			if matchurl==None:
				continue
			else:
				url= matchurl.group(1)
				matchdomain= re.search(urlBegReg, url)

				if matchdomain ==None:
					continue
				else:
					validString = checkValidity(matchdomain.group(1))
					if validString == None:
						continue
					else:
						print ip +"#" +timestamp +"#"+ getUrl + "#" +ctc.replace('\\','')+ "#"+ validString
		

		except AttributeError:
		#	print "Unable to parse line : \n" + line
			continue


if __name__ == "__main__":
    main()
	
