#!/usr/bin/python

import os, time, sys, random
from threading import Thread
import thread, smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
from datetime import datetime

mozilla_profile_name="u22i0uhs.default"
machine_home=os.environ["HOME"]
firefox_log_location = "/tmp/mozillaLog.log"
flash_log_location = machine_home + "/.macromedia/Flash_Player/Logs/flashlog.txt"
firefox_log_level = "timestamp,nsHttp:5"  #print timestamp and the Http requests only.
flash_debug_conf= "ErrorReportingEnable=1 TraceOutputFileEnable=1 MaxWarnings=50"
test_video_time = 180
buffer_termination_time = 3
term_to_search="error"
flash_configuration_file= machine_home + "/mm.cfg"
error_file_location = "/tmp/playbackerror"  + str(datetime.now().hour) + str(datetime.now().minute)
error_log = "The error log file can be found at " + error_file_location
display_no = 96
mailerlist = ["hanson.wong@cbsinteractive.com", "gaurav.tiwari@cbsinteractive.com"]
fromname="cantesttool@cn-sfo1-ins-csdev2.cnet.com"
safe_mode_lock = machine_home + "/.mozilla/firefox/" + mozilla_profile_name + "/.parentlock"
netexport_log_location = machine_home + "/.mozilla/firefox/" + mozilla_profile_name + "/firebug/netexport/logs/"
flashlines_to_scan = 40

urllist= ["http://www.cbs.com/shows/late_show/video/",
          "http://www.cbs.com/shows/2_broke_girls/video",
          "http://www.cbs.com/shows/big_bang_theory/video",
          "http://www.cbs.com/shows/the_good_wife/video"
         ]
firefox_url=urllist[random.randrange(0,len(urllist) -1)]



def set_virtual_display():
    os.system("Xvfb :" + str(display_no))
    time.sleep(2)

def clear_logs():
    print "clearing logs"
    os.system("rm "+ firefox_log_location)
    os.system("rm "+ flash_log_location)
    os.system("rm "+ safe_mode_lock)
    os.system("rm -f " + netexport_log_location + "*")

def set_environment():
    flash_config_file = open(flash_configuration_file, 'w')
    flash_config_file.write(flash_debug_conf)
    flash_config_file.close()
    os.environ["NSPR_LOG_FILE"]=firefox_log_location
    os.environ["NSPR_LOG_MODULES"] = firefox_log_level
    #os.environ["DISPLAY"]= ":" + str(display_no)

def executefirefox():
    os.system("firefox --new-window=" + firefox_url)

def print_firefox_log():
    firefox_log = open(firefox_log_location, 'r')
    error_file_handle.write("Error Report")
    error_file_handle.write("------------------------Mozilla Log -----------------------\n")
    for line in firefox_log:
        try:
            line.decode('ascii')
            error_file_handle.write(line)
        except UnicodeDecodeError:
            continue
    firefox_log.close();

def print_flash_log():
    flash_log_file = open(flash_log_location, 'r')
    error_file_handle.write("------------------------Flash Log -----------------------\n")
    for line in flash_log_file:
        error_file_handle.write(line)
    error_file_handle.flush()
    flash_log_file.close()

def print_netexport_log():
    listing = os.listdir(netexport_log_location)
    error_file_handle.write("------------------------Mozilla NetExport Log -----------------------\n")
    for file in listing:
        netexport_log= open(netexport_log_location + file, 'r')
        for line in netexport_log:
            error_file_handle.write(line)
        error_file_handle.flush()
        netexport_log.close()
        break


def failed_playback():
    print_netexport_log()
    print_flash_log()
    send_mail(fromname, mailerlist, "Video Playback Test Failed , Host: csdev2a, Time: " + str(datetime.now().hour) + ":" + str(datetime.now().minute) , "Video PlayBack Test failed see log attached")
    print error_log

def send_mail(send_from, send_to, subject, text, server="localhost"):
    assert type(send_to)==list

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach( MIMEText(text) )
    part = MIMEBase('application', "octet-stream")
    part.set_payload( open(error_file_location,"rb").read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(error_file_location))
    msg.attach(part)
    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

def tail( f, window=20 ):
    BUFSIZ = 1024
    f.seek(0, 2)
    bytes = f.tell()
    size = window
    block = -1
    data = []
    while size > 0 and bytes > 0:
        if (bytes - BUFSIZ > 0):
            f.seek(block*BUFSIZ, 2)
            data.append(f.read(BUFSIZ))
        else:
            f.seek(0,0)
            data.append(f.read(bytes))
        linesFound = data[-1].count('\n')
        size -= linesFound
        bytes -= BUFSIZ
        block -= 1
    return '\n'.join(''.join(data).splitlines()[-window:])



#set_virtual_display()
clear_logs()
set_environment()
t= Thread(target=executefirefox)
t.start()
time.sleep(test_video_time)
os.system("killall firefox")
time.sleep(buffer_termination_time)
error_file_handle = open(error_file_location, 'w')
return_code=0
try:
    flash_log_file = open(flash_log_location, 'r')
    for line in flash_log_file :
        if term_to_search in line.lower():
            flash_log_file.close()
            failed_playback()
            return_code=2
            break
except IOError:
    error_file_handle.write("The flash log was not created. ie; Either there is no network connectivity or the swf did not load.")
    print_firefox_log()
    print error_log
    return_code=2

error_file_handle.close()

if return_code==0:
    print "OK - Video Playing Successfully."
    os.system("rm "+ error_file_location)

sys.exit(return_code)
