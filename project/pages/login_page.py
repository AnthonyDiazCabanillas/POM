from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .home_page import HomePage 

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://citaweb.clinicasanfelipe.com/CSF_CITAS/" 
        
        # Busca los localizadores
        self.USERNAME_FIELD = (By.ID, "txtDni")
        self.PASSWORD_FIELD = (By.ID, "txtClave")
        self.LOGIN_BUTTON = (By.ID, "btnLogin")
    
    def open(self):
        """Abre la página de login"""
        self.driver.get(self.url)
        self.driver.maximize_window()
        return self
    
    def enter_credentials(self, username, password):
        """Ingresa credenciales de usuario"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.USERNAME_FIELD)
        ).send_keys(username)
        
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        return self
    
    def submit_login(self):
        """Hace clic en el botón de login"""
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return HomePage(self.driver)