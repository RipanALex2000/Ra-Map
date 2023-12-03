import string
import requests
from bs4 import BeautifulSoup

from hashlib import new
import smtplib
sender="s96840880@gmail.com"
subject="Testez acest program frumos"
to_addr_list=['r22724104@gmail.com']
cc_addr_list=['']
def sendemail(sender,message,subject,to_addr_list,cc_adrr_list=[]):
    try:
        smtpserver='smtp.gmail.com:587'
        header='From: %s\n' % sender
        header+='To: %s\n' % ','.join(to_addr_list)
        header+='CC: %s\n' % ','.join(cc_adrr_list)
        header+='Subject: %s\n\n' % subject
        message=header+message
        server=smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(sender,"tdni auke exza jrlj ")
        server.sendmail(sender, to_addr_list, message)
        print("Done")
        server.quit()
        return True
    except:
        print("Error:unable to send email")
        return False
#sendemail(sender,"Pretul a scazut la:",subject,to_addr_list,cc_addr_list,)
def data_scraping():
        req=requests.get("https://www.emag.ro/search/iphone%2014?ref=effective_search")
        soup=BeautifulSoup(req.text,"html.parser")
        price=soup.find('p',attrs={'class': 'product-new-price'}).text
        new_price=price[0:5]
        new_price=new_price.replace(".","")
        new_price=int(new_price)
        pret_referinta=4000
        if(new_price<pret_referinta):
             sendemail(sender,"Pretul a scazut la: "+str(new_price),subject,to_addr_list,cc_addr_list)
             print("Pretul a scazut")
        else:
             print("Pretul nu a scazut")
data_scraping()