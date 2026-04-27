import pytest
import os
from utils.driver_factory import create_driver
from pages.login_page import LoginPage

@pytest.fixture

def driver():
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    return driver

@pytest.hookimpl(hookwrapper=True)

def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs["driver"]
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        driver.save_screenshot(f"{screenshot_dir}/{item.name}.png")