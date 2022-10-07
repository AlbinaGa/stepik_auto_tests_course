from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link1 = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link1)

    button1 = browser.find_element(by='css selector', value='button.btn')
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_windowmodul2_lesson3_step4.py)
    x_element = browser.find_element(by='id', value='input_value')
    x = x_element.text
    y = calc(x)
    input = browser.find_element(by='id', value='answer')
    input.send_keys(y)

    button2 = browser.find_element(by='css selector', value='button.btn')
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

