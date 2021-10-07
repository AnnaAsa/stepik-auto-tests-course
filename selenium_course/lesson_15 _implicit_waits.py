from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome(executable_path=r'C:\Tools\Browsers_Drivers\chromedriver.exe')
    browser.implicitly_wait(15)
    browser.get(link)

    lowPrice = WebDriverWait(browser, 10).until(text_to_be_present_in_element((By.ID, "price"), "100"))
    book = browser.find_element_by_xpath("//button[@id='book']")
    book.click()
   

    x = calc(newstr)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
