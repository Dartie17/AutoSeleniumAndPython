# Вкладки браузера

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button_1 = browser.find_element(By.CSS_SELECTOR, "button")
    button_1.click()

    # Указываем вторую вкладку с индексом "1"
    new_window = browser.window_handles[1]
    # Переключаемся на вторую вкладку
    browser.switch_to.window(new_window)

    num_element = browser.find_element(By.ID, "input_value")
    num = num_element.text

    answer = calc(num)

    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(answer)

    button_2 = browser.find_element(By.CLASS_NAME, "btn-primary")
    button_2.click()

    alert_2 = browser.switch_to.alert
    print(alert_2.text)

finally:
    browser.quit()
