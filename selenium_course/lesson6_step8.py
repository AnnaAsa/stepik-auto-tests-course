from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome(executable_path=r'C:\Tools\Browsers_Drivers\chromedriver.exe')
    browser.get(link)

    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    browser.find_element_by_css_selector('#answer').send_keys(y)
    browser.find_element_by_css_selector('#robotCheckbox').click()
    browser.find_element_by_css_selector('#robotsRule').click()
    browser.find_element_by_xpath('//button[text()="Submit"]').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
