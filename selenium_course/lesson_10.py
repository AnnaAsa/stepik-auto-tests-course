from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome(executable_path=r'C:\Tools\Browsers_Drivers\chromedriver.exe')
    browser.get(link)
    x = browser.find_element_by_xpath("//span[@id='num1']").text
    y = browser.find_element_by_xpath("//span[@id='num2']").text

    num1 = int(x)
    num2 = int(y)
    sum_int = num1 + num2
    sum_str = str(sum_int)

    browser.find_element_by_xpath('//select[@id="dropdown"]').click()
    browser.find_element_by_css_selector("[value='" + sum_str + "']").click()
    browser.find_element_by_xpath('//button[@type="submit"]').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
