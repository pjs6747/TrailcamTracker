import os
import urllib.request
import smtplib
import ssl
import time


def getIP ():
    ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return ip;


def sendIP ():
    port = 465
    password = 'Lancer57'

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("psipgrabber@gmail.com", password)
        message = 'Your sd card has been access from the ip address %s'

        server.sendmail('psipgrabber@gmail.com', 'pdiddyboi2857@gmail.com', message %getIP())


def main():
    sendIP()
    print("YOUR PUBLIC IP ADDRESS HAS BEEN SHARED WITH THE OWNER OF THIS SD CARD")
    time.sleep(15)




main()