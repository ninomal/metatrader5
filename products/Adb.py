import time
import urllib
import os
from products.Screenshot import Screenshot
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

# BETA
class Adbconect():
   
    def __init__(self, PHONENUMBER, product, ui) -> None:
        self.PHONENUMBER = PHONENUMBER
        self.driver = webdriver.Chrome()
        self.screnshoot = Screenshot(product, ui)
        

    def adbConect(self):
        # Creating the driver (browser)
        self.driver.maximize_window()
        self.driver.get("https://web.whatsapp.com/")
        conect = False
        while conect != True:
            conect = bool(self.driver.find_elements(By.XPATH, 
                '//*[@id="app"]/div/div[2]/div[3]/header/div[2]/div/span/div[5]/div/span'))
            time.sleep(1.0)
            print("1")
        time.sleep(5.0) 
        myself = self.driver.find_element(By.ID, 'Meu Numero')
        myself.click()
        time.sleep(3.0)
        print("teste myself")
        time.sleep(3.0)
        self.sendMsg()
        
        
    def sendMsg(self):
        text = "hello world"
        text = urllib.parse.quote(text)
        #send_link = f"https://web.whatsapp.com/send?phone={self.PHONENUMBER}&text={text}"
        #self.driver.get(send_link)
        time.sleep(12.0)
        self.sendImagens("click.png")
        self.clickSend()
        print("2")
        
        #click
    def clickSend(self):
        #driver.find_element(By.XPATH,).click()
        print(3)
        localClick = pyautogui.locateCenterOnScreen("products\click.png")
        pyautogui.click(localClick[0], localClick[1])
        time.sleep(4.0)
        print(4)
        
        #read msg in closed chat
    def readMsgOfBoard(self):
        read = self.driver.find_element(By.CLASS_NAME, '_2KKXC ')
        time.sleep(3.0)
        print(read.text)
        

        # Close the browser
    def closedWeb(self):
        print(5)
        time.sleep(12.0)
        self.driver.quit()
        
    def sendImagens(self, pathImg):  
        img = self.driver.find_element(By.ID, 'attach-menu-plus')
        img.click()
        img = self.driver.find_element(By.CLASS_NAME, 'lhggkp7q qq0sjtgm tkdu00h0 ln8gz9je')
        img.click()
        img.send_keys(pathImg)
        time.sleep(15.0)
        self.clickSend()
        print("testee img")