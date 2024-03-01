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
        time.sleep(10.0)
        user_name = "Meu Numero"
        #In above variable at place of `Anurag Kushwaha` pass Name or number of Your Teacher
        # who going to sent you zoom meeting link same as you have in your contact list.
        time.sleep(5.0)
        try:
            #user = self.driver.find_element(By.PARTIAL_LINK_TEXT,'//span[@title="{}"]'.format(user_name))
            #user.click()
        # For getting message to perform action 
            message = self.driver.find_element(By.CLASS_NAME, "cm280p3y to2l77zo n1yiu2zv c6f98ldp ooty25bp oq31bsqd") 
        # In the above line Change the xpath's class name from the current time class name by inspecting span element
        # which containing received text message of any chat room.
            for i in message:
                try:
                    print("teste")
                    if "zoom.us" in str(i.text):
                    # Here you can use you code to preform action according to your need
                        print("Perform Your Action")
                except:   
                    pass
            
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
        