import time
import urllib
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

# BETA
class Adbconect():
   
    def __init__(self, PHONENUMBER, product, ui) -> None:
        self.PHONENUMBER = PHONENUMBER
        self.driver = webdriver.Chrome()
        
    def adbConect(self):
        # Creating the driver (browser)
        self.driver.maximize_window()
        self.driver.get("https://web.whatsapp.com/")
        conect = False
        while conect != True:
            conect = bool(self.driver.find_elements(By.XPATH, 
                '//*[@id="app"]/div/div[2]/div[3]/header/div[2]/div/span/div[5]/div/span'))
            time.sleep(1.0)
        time.sleep(3.0)
        #Open chat here
        self.sendMsgStandard("Open chat")
        time.sleep(13.0)
        print("teste myself")
        self.sendMsg('Finish?')
        self.readMsgOfChat()
        print("of chat ^ on chat v")
        self.readMsgOnChat()
        time.sleep(3.0)
        self.sendMsg("gg")
              
    def sendMsg(self, textStr):
        text = urllib.parse.quote(textStr)
        time.sleep(12.0)
        self.sendMsgStandard(text)
        self.clickSendMsg()
        
        #click in Msg
    def clickSendMsg(self):
        #driver.find_element(By.XPATH,).click() <- another away 
        print(3)
        localClick = pyautogui.locateCenterOnScreen("products\click.png")
        pyautogui.click(localClick[0], localClick[1])
        time.sleep(4.0)
        
    def clickSendImg(self): 
        time.sleep(6.0)   
        self.driver.find_element(By.XPATH,
        '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span').click() 
        
        #standard text not converted input
    def sendMsgStandard(self, textUrll):
        send_link = f"https://web.whatsapp.com/send?phone={self.PHONENUMBER}&text={textUrll}"
        self.driver.get(send_link)
        
        #read msg in closed chat
    def readMsgOfChat(self):
        read = self.driver.find_element(By.CLASS_NAME, '_2KKXC ')
        time.sleep(3.0)
        print(read.text)
        
        #Beta read msg in chat open 
    def readMsgOnChat(self): 
        read = self.driver.find_elements(By.CLASS_NAME, 'row')
        time.sleep(3.0)
        print(len(read))
        #read = read[0]
        #print(read.text)
        print("Read teste 2")
        #_1DETJ copyable-text
        #span
        # _11JPr selectable-text copyable-text
        #_1DETJ copyable-text
        
        # Close the browser
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
        print("testee img")