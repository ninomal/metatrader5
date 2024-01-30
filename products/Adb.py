import time
import urllib
import os
from Screenshot import Screenshot

from selenium import webdriver
from selenium.webdriver.common.by import By


# BETA
class Adbconect():
   
    def __init__(self, PHONENUMBER, product) -> None:
        self.PHONENUMBER = PHONENUMBER
        self.driver = webdriver.Chrome()
        self.screnshoot = Screenshot(product)

    def adbConect(self):
        # Creating the driver (browser)
        self.driver.maximize_window()
        self.driver.get("https://web.whatsapp.com/")
        time.sleep(20.0)
        print("1")
        
    def sendMsg(self):
        text = "hello world"
        text = urllib.parse.quote(text)
        send_link = f"https://web.whatsapp.com/send?phone={self.PHONENUMBER}&text={text}"
        self.driver.get(send_link)
        time.sleep(12.0)
        print("2")
        #click
    def clickSend(self):
        #driver.find_element(By.XPATH,).click()
        pass
        
    def readMsg(self):
        pass   

        # Close the browser
    def closedWeb(self):
        self.driver.quit()