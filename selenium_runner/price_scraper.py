from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


def extract_price(url):
    options=Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    
    driver=webdriver.Chrome(options=options)
    
    try:
        driver.get(url)
        #time.sleep(6)
        price_element=driver.find_element(By.CLASS_NAME,"a-price-whole")
        return price_element.text

    except Exception as e:
        print(f"Error :{e}")

    finally:
        driver.quit()        


