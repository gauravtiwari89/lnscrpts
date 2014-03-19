import urllib2, sys 
from random import randint
from threading import Thread
import thread, smtplib


threshold = 70000000
id1 = 0

def write(userId, contentId, facebookPostId):
	
	global id1
	id1 = id1  + 1

	if id1> threshold:
		sys.exit()
	else:

		if facebookPostId==None:
			response = urllib2.urlopen("http://localhost:8080/api/v2.0/activityfeed/add.json?cid="+ str(contentId) +"&user="+str(userId) +"&fbid=abcd1")		

		else:
			response = urllib2.urlopen("http://localhost:8080/api/v2.0/activityfeed/add.json?cid="+ str(contentId) +"&user="+str(userId) +"&fbid=abcd2")	



def addrandomly():
	contentId= randint(100000, 105000)

	userId = randint(1, 20000000)

	facebookPostId  = randint(0,1)
	if facebookPostId==0:
		facebookPostId=None

	write(userId, contentId, facebookPostId)		






def execute():
	while(True):
		addrandomly()


t= Thread(target=execute)
t1= Thread(target=execute)
t2= Thread(target=execute)
t3= Thread(target=execute)
t4= Thread(target=execute)
t5= Thread(target=execute)
t6= Thread(target=execute)
t7= Thread(target=execute)
t8= Thread(target=execute)
t9= Thread(target=execute)
t11= Thread(target=execute)
t12= Thread(target=execute)
t13= Thread(target=execute)
t14= Thread(target=execute)
t15= Thread(target=execute)
t16= Thread(target=execute)
t17= Thread(target=execute)
t18= Thread(target=execute)
t19= Thread(target=execute)



t.start()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()


t11.start()
t12.start()
t13.start()
t14.start()
t15.start()
t16.start()
t17.start()
t18.start()
t19.start()


