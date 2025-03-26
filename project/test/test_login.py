import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage #IMPORTAR LA CLASE QUE SE creo

def test_login():
    driver = webdriver.Chrome()
    
    try:
        login_page = LoginPage(driver)
        (login_page.open()
                  .enter_credentials("74847349", "Tonydc1502%")
                  .submit_login())
        time.sleep(8)
    finally:

        citas=driver.find_element(By.ID,"img_INI_HistorialCitas")
        citas.click()
        time.sleep(100000)
        driver.quit()

if __name__ == "__main__":
    test_login()