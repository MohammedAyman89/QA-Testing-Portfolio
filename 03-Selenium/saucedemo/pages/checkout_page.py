from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.finish_btn = (By.ID, "finish")
        self.title = (By.CLASS_NAME, "title")
        self.complete_message = (By.CLASS_NAME, "complete-header")

    def fill_info(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.zip_code).send_keys(zip_code)

    def click_continue(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_btn)
        ).click()

    def click_finish(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish_btn)
        ).click()

    def get_title(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.title)
        ).text

    def get_complete_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.complete_message)
        ).text
