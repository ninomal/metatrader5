import time
import urllib
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

# BETA
class Adbconect():
    def __init__(self, PHONENUMBER):
        self.PHONENUMBER = PHONENUMBER
        self.conect = False
        
        # Creating the driver (browser)
    def adbConect(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://web.whatsapp.com/")
        while self.conect != True:
            self.conect = bool(self.driver.find_elements(By.XPATH, 
                '//*[@id="app"]/div/div[2]/div[3]/header/div[2]/div/span/div[5]/div/span'))
            time.sleep(1.0)
        time.sleep(3.0)
        #Open chat here
        self.sendMsg('Finish?')
        #self.readMsgOfChat()
        #print("of chat ^ on chat v")
        #self.readMsgOnChat()
        
              
    def sendMsg(self, textStr):
        text = urllib.parse.quote(textStr)
        time.sleep(12.0)
        self.sendMsgStandard(text)
        time.sleep(6.0)
        
        #click in Msg
    def clickSendMsg(self):
        self.driver.find_element(By.XPATH,
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click() 
        #localClick = pyautogui.locateCenterOnScreen("products\click.png")
        #pyautogui.click(localClick[0], localClick[1])
        #time.sleep(4.0)
        
    def clickSendImg(self): 
        time.sleep(10.0)   
        self.driver.find_element(By.XPATH,
        '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span').click() 
        
        #standard text not converted input
    def sendMsgStandard(self, textUrll):
        send_link = f"https://web.whatsapp.com/send?phone={self.PHONENUMBER}&text={textUrll}"
        while self.conect != True:
            self.conect = bool(self.driver.find_elements(By.XPATH, 
                '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div/div/div/div/span'))
            time.sleep(1.0)
        self.driver.get(send_link)
        
        #read msg of chat
    def readMsgOfChat(self):
        #readHtml = self.driver.find_element(By.)
        read = self.driver.find_element(By.CLASS_NAME, '_2KKXC ')
        time.sleep(3.0)
        print(read.text)
        
        #Beta read msg in chat open 
    def readMsgOnChat(self): 
        time.sleep(8.0)
        try:
            message = self.driver.find_element(By.XPATH,
        '//*[@id="main"]/div[3]/div/div[2]/div[3]/div[20]/div/div/div[1]') 
            print(message.text)
            for i in range(20, 24):    
                print(i)
                xpath = f'//*[@id="main"]/div[3]/div/div[2]/div[3]/div[{i}]/div/div/div[1]'
                message = self.driver.find_element(By.XPATH, xpath)
                try:
                    print(message.text)
                except:
                    print("error msg")        
        except:
            print("Error read msg")
            
    def closedWeb(self):
        time.sleep(12.0)
        self.driver.quit()
        
        #send imagen 
    def sendImagens(self, pathImg):  
        img = self.driver.find_element(By.XPATH, 
         '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
        time.sleep(4.0)
        img = self.driver.find_element(By.XPATH,
         '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input')
        time.sleep(3.0)
        absImg =  os.path.abspath(pathImg)
        img.send_keys(absImg)
        self.clickSendImg()
        time.sleep(10.0)
        