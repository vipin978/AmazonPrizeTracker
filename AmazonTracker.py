import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/JBL-T205BT-Wireless-Earbud-Headphones/dp/B07B9CS9FQ/ref=sr_1_11?crid=7WCVBWY9U96F&keywords=jbl+bluetooth+headphones+original&qid=1584287129&sprefix=jbl+bluetooth+%2Caps%2C475&sr=8-11'
headers = {
    "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

def sendMail():
    
    # Setting up EMAIL server and start listening in port 587
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    # Email we are going to operate ON 
    server.login('vipinramar978@gmail.com','vipinasc')
    
    # Preparing the message content to send via Email
    subject = "Hey User the price has dropped down go and visit"
    body = "Check the amazon link ... https://www.amazon.in/JBL-T205BT-Wireless-Earbud-Headphones/dp/B07B9CS9FQ/ref=sr_1_11?crid=7WCVBWY9U96F&keywords=jbl+bluetooth+headphones+original&qid=1584287129&sprefix=jbl+bluetooth+%2Caps%2C475&sr=8-11"
    MSG = f"{subject}\n\n{body}"
    
    # Sending the mail
    server.sendmail(
        'vipinramar978@gmail.com',
        '17tucs251@skct.edu.in',
        MSG
    )
    
    # For Debugging purposes
    print("Mail has been sent")


def checkPrize():
    
    # It will get the HTML page to parse
    page = requests.get(URL,headers = headers).text
    
    # Parse the HTML and extract INFO
    parse = BeautifulSoup(page,'lxml')
    title = parse.find(id = "productTitle").get_text()
    price = parse.find(id = "priceblock_ourprice").get_text()
    
    #If we attain the required price then we will send mail 
    extractedPrice= int(price[4:7])+1000
    if extractedPrice < 1000:
        sendMail()

checkPrize()    


