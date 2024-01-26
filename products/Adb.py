import time

from selenium import webdriver


# Creating the driver (browser)
driver = webdriver.Firefox()
driver.maximize_window()

driver.quit()