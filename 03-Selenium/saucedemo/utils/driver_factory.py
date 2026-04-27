from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver():
    options = Options()

    #Isolate Session
    options.add_argument("--incognito")

    #Start Browser
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    return driver