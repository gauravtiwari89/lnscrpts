# -*- coding: utf-8 -*-
import sys, re, smtplib, imaplib, email
from datetime import date, datetime, timedelta
import glob, gzip, operator, os
import urllib2, cookielib
from collections import defaultdict
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
from sets import Set
from BeautifulSoup import *
from readability.readability import Document



mailerlist = ["gauravtiwari89@gmail.com"]
login_name=""
gmailPassword = ''
from_name="Read-Later-Articles."
urlset = Set([])
email_string =""
counter = 0

def cleanSoup(val):
    
    soup = BeautifulSoup(val)
    all_text = ''.join(soup.findAll(text=True))
    return all_text


def send_mail(send_from, send_to, subject, text, server="smtp.gmail.com"):
    assert type(send_to)==list
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach( MIMEText(text) )
    
    smtp = smtplib.SMTP(server, 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(login_name, gmailPassword)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

def extract_body(payload):
    if isinstance(payload,str):
        return payload
    else:
        return '\n'.join([extract_body(part.get_payload()) for part in payload])
    
    

def getTextFromURL(urlcoll):
    global email_string, counter
    for url in urlcoll:
        try:
            html = urllib2.urlopen(url).read()
            readable_article = Document(html).summary()
            readable_title = Document(html).short_title()
            email_string = email_string + readable_title.upper() + "\n\n"
            email_string = email_string  + removeNonAscii(cleanSoup(readable_article)) + "\n\n====================================================\n\n\n"
            counter = counter + 1
        except:
            None
        


conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
conn.login(login_name, gmailPassword)
conn.select()
typ, data = conn.search(None, 'UNSEEN')

try:
    for num in data[0].split():
        typ, msg_data = conn.fetch(num, '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1])
                payload=msg.get_payload()
                body=cleanSoup(extract_body(payload))
                urllist  = re.findall(r'http[s]?://[^\s<>"]+|www\.[^\s<>"]+', str(body))
                if urllist!=None:
                    for url in urllist:
                        urlset.add(url)
        
        typ, response = conn.store(num, '+FLAGS', r'(\Seen)')

    getTextFromURL(urlset)

finally:
    try:
        conn.close()
    except:
        pass
    conn.logout()



if email_string:
    send_mail(from_name, mailerlist, "Total links :  " + str(counter) + ".  " + str(datetime.now().month)+"-"+str(datetime.now().day)+"/"+str(datetime.now().hour), email_string)
