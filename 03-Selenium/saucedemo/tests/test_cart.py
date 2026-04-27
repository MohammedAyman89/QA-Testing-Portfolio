from pages.Inventory_Page import InventoryPage
from pages.cart_page import CartPage

EXPECTED_PRODUCTS = [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)"
]

def test_item_in_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_to_cart(EXPECTED_PRODUCTS[0])
    cart_page = CartPage(logged_in_driver)
    cart_page.open_cart()
    assert EXPECTED_PRODUCTS[0] in cart_page.get_cart_items()

def test_remove_item(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_to_cart(EXPECTED_PRODUCTS[0])
    inventory_page.add_to_cart(EXPECTED_PRODUCTS[1])
    cart_page = CartPage(logged_in_driver)
    cart_page.open_cart()
    cart_page.remove_item(EXPECTED_PRODUCTS[0])
    assert cart_page.get_cart_items() == [EXPECTED_PRODUCTS[1]]

def test_checkout(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_to_cart(EXPECTED_PRODUCTS[0])
    cart_page = CartPage(logged_in_driver)
    cart_page.open_cart()
    cart_page.checkout()
    assert cart_page.get_cart_message() == "Checkout: Your Information"
