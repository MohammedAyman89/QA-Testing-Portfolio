from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    url = "https://www.saucedemo.com"
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.title = (By.CLASS_NAME, "title")
        self.error_message = (By.CLASS_NAME, "error-message-container")

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self.username).clear()
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).clear()
        self.driver.find_element(*self.password).send_keys(password)
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
            ).click()
        

    def get_message(self):

        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.title)
            ).text
    
    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_message)
            ).text
        