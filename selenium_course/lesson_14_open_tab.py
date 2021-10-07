from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome(executable_path=r'C:\Tools\Browsers_Drivers\chromedriver.exe')
    browser.get(link)

    trollButton = browser.find_element_by_xpath("//button[@class='trollface btn btn-primary']")
    trollButton.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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
