import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


link ="http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.NAME, "firstname").send_keys("Ivan")
browser.find_element(By.NAME, "lastname").send_keys("Ivanov")
browser.find_element(By.NAME, "email").send_keys("Ivan@mail.ru")

file = browser.find_element(By.CSS_SELECTOR, "[type='file']")
file.send_keys(f"{os.getcwd()}/Scripts/file.txt")

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
browser.find_element(By.CSS_SELECTOR,"[type='submit']").click()
alert = browser.switch_to.alert
print(alert.text)

browser.quit()




