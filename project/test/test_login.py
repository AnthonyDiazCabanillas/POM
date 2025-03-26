import sys
import os
import time
from selenium import webdriver

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage

def test_login():
    driver = webdriver.Chrome()
    
    try:
        login_page = LoginPage(driver)
        (login_page.open()
                  .enter_credentials("74847349", "Tonydc1502%")
                  .submit_login())
        time.sleep(100000)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login()