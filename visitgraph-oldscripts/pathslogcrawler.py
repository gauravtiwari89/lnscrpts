#!/usr/bin/python

import sys, base64, re
import json, collections


pattern=	r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*\[(.*)\].*\"((GET|POST)\s([a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+).*CBS_CTC=(.*)'					
patternUrl= 	r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)'
urlbeg = r'http[s]?://?www.cbs.com(\/.*)'   
fetchdecimal = r'(.*)\/(\d{1,11})\/?$'	# regular expression to trap a decimal at the end of the string. 


regx = re.compile(pattern) 
urlRegx= re.compile(patternUrl)
urlBegReg = re.compile(urlbeg)
fetchdecimalReg = re.compile(fetchdecimal)

def decodePayload(payload):
        return base64.b64decode(payload)


def processCTC(ctc):
        #only returning uuid till the log structure is more robust.     
        return ctc.split('|')[0]



def checkValidity(url):
	
	if "com/primetime" in url: 
		return None
	elif "com/daytime" in url: 
		return None
	elif "com/latenight" in url: 
		return None
	elif "sitesearch" in url: 
		return None
	elif "reset/password" in url: 
		return None
	elif "com/check-in/getButton" in url:
		return None
	elif "cbs.com/e/" in url: 
		return None
	elif "caraosels" in url: 
		return None
        elif "/video/" in url:
                return url[0:url.index("/video/") + 7]
	elif "/week/" in url:
                return url[0:url.index("/week/")]
        elif "/photos/" in url:
                return url[0:url.index("/photos/") + 8]    # adding 8 to include "/photos/ in the resulting url"
        elif "/forum/" in url:
                return url[0:url.index("/forum/") + 7 ]
	elif "/week/" in url:
		return url[0:url.index("/week/")]
        elif "com/cbs_cares" in url: 
		return "http://www.cbs.com/cbs_cares/"
	elif "/episodes" in url:
                return url[0:url.index("/episodes") + 9]    # adding 9 to include "episodes"
        elif "/Episodes" in url:
                return url[0:url.index("/Episodes") + 9]
        elif "/cast" in url:
                return url[0:url.index("/cast") + 5]       # adding 6 to include cast
        elif "recaps/" in url:
                return  url[0:url.index("recaps/")] + "recaps/index.php"
        elif "?" in url:
                return url[0:url.index("?")]
        elif "&" in url :
                return url[0:url.index("&")]
        elif "%" in url:
                return url[0:url.index("%")]
	else :
		return url


def postvaliditycheck(url):
	newUrl = checkValidity(url)
	if newUrl == None: 
		return None
	else:

		newUrl=newUrl.replace("//", "/")

		if "." in newUrl[len(newUrl)-10:]:  	# Check for .jpg, .swf etc
			return None

		matchdecimal = re.search(fetchdecimalReg, newUrl)
		if matchdecimal == None: 
			return newUrl
		else:
			return newUrl[0:newUrl.index(matchdecimal.group(2))]
				


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
					validString = postvaliditycheck(matchdomain.group(1))
					if validString == None:
						continue
					else:
						print ip +"#" +timestamp +"#"+ getUrl + "#" +ctc.replace('\\','')+ "#"+ validString
		

		except AttributeError:
		#	print "Unable to parse line : \n" + line
			continue


if __name__ == "__main__":
    main()
	
