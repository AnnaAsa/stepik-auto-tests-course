from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome(executable_path=r'C:\Tools\Browsers_Drivers\chromedriver.exe')
    browser.get(link)
    browser.execute_script("window.scrollBy(0, 100);")
    x = browser.find_element_by_xpath("//span[@id='input_value']").text

    num1 = int(x)

    result = str(math.log(abs(12*math.sin(num1))))

    answer_field = browser.find_element_by_xpath("//input[@id='answer']")
    answer_field.send_keys(result)

    robotCheckbox = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    robotCheckbox.click()
    robotsRule = browser.find_element_by_xpath("//input[@id='robotsRule']")
    robotsRule.click()
    browser.find_element_by_xpath('//button[@type="submit"]').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
