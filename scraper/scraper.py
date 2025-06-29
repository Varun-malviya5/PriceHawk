import sys
import os
import requests
import smtplib
from bs4 import BeautifulSoup
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium_runner.price_scraper import extract_price



URL = 'https://www.amazon.in/Sony-ILCE-7M4K-Full-Frame-Interchangeable-Lens-Mirrorless/dp/B09SB2P8J5/ref=sr_1_4?crid=294YNUVF9VW5G&dib=eyJ2IjoiMSJ9.4tmYppZGNOTWyjJQgwkD0rTIdJmZshIGRonWplQ1JCo0md380CfUyPjgfAUlWS_-yDR4BB-Kn49fxDYDGtO946sq42-cgIvuqsCRhKbdNvcVXKwwtuN5gPbQCKeo2wOa4wztrdr_VaoiMxquQ1R6Ewif-PDCAI28lq2vfkLMh7kb8RZEXKUEaFia-1cStAaZrm9r6JmhvzOBHm68hojhE6zc7N5Sw1BqpwO4ZB5Vx8E.Cl4Pvi9Dws9h3WWNdDHLqd6vMk4AEhIqamKGLAGpNJE&dib_tag=se&keywords=sony%2Ba7&nsdOptOutParam=true&qid=1750315594&sprefix=sony%2Ba7%2Caps%2C886&sr=8-4&th=1'
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}

def check_price():
    page=requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    title=soup.find(id="productTitle").get_text()

    #price=soup.find(id="a-price-whole").get_text()
    #converted_price=price[0:5]
    #print(converted_price)
    url = URL
    price = extract_price(url)
    clean_price=price.replace(",","").strip()
    price_int=int(clean_price)
    if(price_int<250989):
        send_mail()
    print(price_int)
    # converted_price=float(price)
    # print("Price:", converted_price)
    print(title.strip())
 #azic uwlb bwje rvhs
 ##rgvl zrpv iwnx ijay
def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo() 
    email_password = os.environ.get('EMAIL_PASS') 
    server.login('w61931333@gmail.com',email_password)  
    subject='Price fell down!'
    body='Check the Amazon Link: https://www.amazon.in/Sony-ILCE-7M4K-Full-Frame-Interchangeable-Lens-Mirrorless/dp/B09SB2P8J5/ref=sr_1_4?crid=294YNUVF9VW5G&dib=eyJ2IjoiMSJ9.4tmYppZGNOTWyjJQgwkD0rTIdJmZshIGRonWplQ1JCo0md380CfUyPjgfAUlWS_-yDR4BB-Kn49fxDYDGtO946sq42-cgIvuqsCRhKbdNvcVXKwwtuN5gPbQCKeo2wOa4wztrdr_VaoiMxquQ1R6Ewif-PDCAI28lq2vfkLMh7kb8RZEXKUEaFia-1cStAaZrm9r6JmhvzOBHm68hojhE6zc7N5Sw1BqpwO4ZB5Vx8E.Cl4Pvi9Dws9h3WWNdDHLqd6vMk4AEhIqamKGLAGpNJE&dib_tag=se&keywords=sony%2Ba7&nsdOptOutParam=true&qid=1750315594&sprefix=sony%2Ba7%2Caps%2C886&sr=8-4&th=1'
    msg=f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'w61931333@gmail.com',
        'besharam202@gmail.com',
        msg
    )
    print('Hey email has been sent')
    server.quit()
#while(True):
check_price()
    #time.sleep(60*60)


