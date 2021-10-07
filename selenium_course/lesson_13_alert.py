from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome(executable_path=r'C:\Tools\Browsers_Drivers\chromedriver.exe')
    browser.get(link)

    magicButton = browser.find_element_by_xpath("//button[@type='submit']")
    magicButton.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element_by_xpath("//span[@id='input_value']").text
    x = calc(x_element)

    answer = browser.find_element_by_xpath("//input[@id='answer']")
    answer.send_keys(x)
    browser.find_element_by_xpath('//button[text()="Submit"]').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
