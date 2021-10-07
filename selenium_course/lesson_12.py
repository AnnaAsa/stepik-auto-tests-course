import os

from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome(executable_path=r'C:\Tools\Browsers_Drivers\chromedriver.exe')
    browser.get(link)

    firstName = browser.find_element_by_xpath("//input[@name='firstname']")
    firstName.send_keys("Anna")
    lastName = browser.find_element_by_xpath("//input[@name='lastname']")
    lastName.send_keys("Asab")
    email = browser.find_element_by_xpath("//input[@name='email']")
    email.send_keys("email@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    LoadButton = browser.find_element_by_xpath("//input[@name='file']")
    LoadButton.send_keys(file_path)
    submitButton = browser.find_element_by_xpath("//button[@type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
