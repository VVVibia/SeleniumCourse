import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_to_add_product(browser):
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    time.sleep(5)
    assert button != None, "Button not found"


