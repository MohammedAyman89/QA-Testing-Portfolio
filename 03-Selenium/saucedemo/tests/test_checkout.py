import pytest
from pages.Inventory_Page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

EXPECTED_PRODUCTS = [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)"
]

def test_full_checkout(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_to_cart(EXPECTED_PRODUCTS[0])

    cart_page = CartPage(logged_in_driver)
    cart_page.open_cart()
    cart_page.checkout()

    checkout_page = CheckoutPage(logged_in_driver)
    assert checkout_page.get_title() == "Checkout: Your Information"

    checkout_page.fill_info("Mohammed", "Ayman", "12345")
    checkout_page.click_continue()
    assert checkout_page.get_title() == "Checkout: Overview"

    checkout_page.click_finish()
    assert checkout_page.get_complete_message() == "Thank you for your order!"


@pytest.mark.negative
@pytest.mark.parametrize("first_name,last_name,zip_code,expected_error", [
    ("", "", "", "First Name is required"),
    ("Mohammed", "", "12345", "Last Name is required"),
    ("Mohammed", "Ayman", "", "Postal Code is required"),
], ids=[
    "all_fields_empty",
    "last_name_empty",
    "postal_code_empty",
])
def test_checkout_empty_fields(logged_in_driver, first_name, last_name, zip_code, expected_error):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_to_cart(EXPECTED_PRODUCTS[0])

    cart_page = CartPage(logged_in_driver)
    cart_page.open_cart()
    cart_page.checkout()

    checkout_page = CheckoutPage(logged_in_driver)
    checkout_page.fill_info(first_name, last_name, zip_code)
    checkout_page.click_continue()

    error_text = checkout_page.driver.find_element(
        "css selector", "[data-test='error']"
    ).text
    assert expected_error in error_text
