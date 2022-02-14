from bs4 import BeautifulSoup
import requests
import schedule
import time
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os

url = "https://weather.com/weather/tenday/l/a05baa5a94807b678c0d9403cbc131381e2b33af1f6264959d7543eaa3b8ed7e"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

print(soup.title.text)

temp = soup.find_all('span', attrs={'class': 'DailyContent--temp--3d4dn'})
print(temp[0].text)
print(temp[1].text)
print(temp[2].text)
print(temp[3].text)
print(temp[4].text)
print(temp[5].text)
print(temp[6].text)
print(temp[7].text)
print(temp[8].text)
print(temp[9].text)
print(temp[10].text)

#import smtplib

# gmail_user = 'cjnsoftware@gmail.com'
# gmail_password = 'CJNSOFTWARE'

# sent_from = gmail_user
# to = ['amazingg500@gmail.com']
# subject = 'Weather Update'
# body = 'Daily Weather Update'

# email_text = """\
# From: %s
# To: %s
# Subject: %s

# %s
# """ % (sent_from, ", ".join(to), subject, body)

# try:
#     smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     smtp_server.ehlo()
#     smtp_server.login(gmail_user, gmail_password)
#     smtp_server.sendmail(sent_from, to, email_text)
#     smtp_server.close()
#     print ("Email sent successfully!")
# except Exception as ex:
#     print ("Something went wrong….",ex)

import smtplib 
try: 
    #Create your SMTP session 
    smtp = smtplib.SMTP('smtp.gmail.com', 587) 

   #Use TLS to add security 
    smtp.starttls() 

    #User Authentication 
    smtp.login("cjnsoftware@gmail.com","CJNSOFTWARE")

    #Defining The Message 
    message = "Weather Update" 

    #Sending the Email
    smtp.sendmail("cjnsoftware@gmail.com", "amazingg500@gmail.com",message) 

    #Terminating the session 
    smtp.quit() 
    print ("Email sent successfully!") 

except Exception as ex: 
    print("Something went wrong....",ex)