import pytest
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

def test_products_names(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    assert inventory_page.get_product_names() == EXPECTED_PRODUCTS

def test_add_to_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_to_cart(EXPECTED_PRODUCTS[0])
    inventory_page.add_to_cart(EXPECTED_PRODUCTS[1])
    assert inventory_page.get_cart_count() == '2'

def test_open_cart(logged_in_driver):
    cart_page = CartPage(logged_in_driver)
    cart_page.open_cart()
    assert cart_page.get_cart_message() == "Your Cart"    
