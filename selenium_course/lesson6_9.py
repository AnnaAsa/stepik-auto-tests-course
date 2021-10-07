from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome(executable_path=r'C:\Tools\Browsers_Drivers\chromedriver.exe')
    browser.get(link)

    treasureChest = browser.find_element_by_xpath('//img[@id="treasure"]')
    x_element = treasureChest.get_attribute('valuex')

    y = calc(x_element)

    browser.find_element_by_css_selector('#answer').send_keys(y)
    browser.find_element_by_css_selector('#robotCheckbox').click()
    browser.find_element_by_css_selector('#robotsRule').click()
    browser.find_element_by_xpath('//button[text()="Submit"]').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
