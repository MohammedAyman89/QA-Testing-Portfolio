from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    def get_product_names(self):
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [product.text for product in products]
        
    def add_to_cart(self, product_name):
        product_id = product_name.lower().replace(' ','-')
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, f"add-to-cart-{product_id}"))
            ).click()
        
    def get_cart_count(self):
        return self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    




    