import time

from selenium import webdriver

from simon.accounts.pages import LoginPage
from simon.header.pages import HeaderPage
from simon.pages import BasePage

# Creating the driver (browser)
driver = webdriver.Firefox()
driver.maximize_window()

# 1. Login
#       and uncheck the remember check box
#       (Get your phone ready to read the QR code)
login_page = LoginPage(driver)
login_page.load()
login_page.remember_me = False
time.sleep(7)


# 2. The base page is inherited by all pages
#       and here you can check whether any
#       page is available on the screen of
#       the browser.

# we don't need to load the pages as whatsapp
# web works as one-page web app
base_page = BasePage(driver)
base_page.is_title_matches()
base_page.is_welcome_page_available()
base_page.is_nav_bar_page_available()
base_page.is_search_page_available()
base_page.is_pane_page_available()
# chat is only available after you open one
base_page.is_chat_page_available()


# 3. Logout
header_page = HeaderPage(driver)
header_page.logout()

# Close the browser
driver.quit()