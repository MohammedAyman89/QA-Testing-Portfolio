import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
@pytest.mark.parametrize("username,password,expected", [
    ("standard_user", "secret_sauce", "Products"),
 ], ids=[
        "valid_login"
 ])

def test_valid_login(driver, username, password, expected):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    assert expected in login_page.get_message()

@pytest.mark.negative
@pytest.mark.parametrize("username,password,expected", [
    ("standard_user", "wrong_pass", "Username and password do not match any user in this service"),
    ("wrong_username", "secret_sauce", "Username and password do not match any user in this service"),
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "", "Password is required"),
    ("locked_out_user", "secret_sauce", "locked out"),
    ("standard_user ", "secret_sauce", "Username and password do not match any user in this service"),
    ("' OR 1=1 --", "anything", "Username and password do not match any user in this service"),
 ], ids=[
        "wrong_password",
        "wrong_username",
        "empty_username",
        "empty_password",
        "locked_user",
        "trailing_space_username",
        "sql_injection"
 ])

def test_Invalid_login(driver, username, password, expected):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    assert expected in login_page.get_error_message()


