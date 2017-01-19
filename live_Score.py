#Created By Gautam 2017-01-19 at 19:37:42
#This is a Testing Python Script
#Lets See What Happens


import urllib2
import urllib
import sys
import os
from bs4 import BeautifulSoup
import time
from twilio.rest import TwilioRestClient

url  ="http://www.cricbuzz.com/"
while True:
    string = ""
    str1 = ""
    try:
        req = urllib2.urlopen(url).read()
        soup = BeautifulSoup(req)
        div = soup.find('div',class_='cb-col-100 cb-col cb-hm-scg-blk ')
        row = div.find('div',class_='cb-col cb-col-25 cb-mtch-blk')
        #for row in div:
        t =  row.find('a')
        str1 = str(t['title'])
        #print string 
        #print t['title']
        k =  row.findAll('div', class_='cb-ovr-flo')[1:6]
        for l in k:
            string = string  + str(l.string) + '\n'
        string = str1 + '\n' +  string
    except:
        continue
    print string
    ACCOUNT_SID = "your_account_id" 
    AUTH_TOKEN = "your_auth_token"

    client = TwilioRestClient(ACCOUNT_SID,AUTH_TOKEN)

    client.messages.create(
        to="mobile_no", 
        from_="twilio_phone_no", 
        body=string,      
    )
    time.sleep(480)
    
