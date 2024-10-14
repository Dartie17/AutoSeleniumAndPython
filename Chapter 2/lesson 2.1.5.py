# Чекбоксы и радиокнопки

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(num):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим значение "x" и вычисляем с его помощью ответ
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    answer = calc(x)

    # Подставляем ответ в нужную строку
    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(answer)

    # Находим чекбокс "Я робот" и активируем его
    option_1 = browser.find_element(By.ID, "robotCheckbox")
    option_1.click()

    # Находим радиокнопку "Robots rule" и активируем ее
    option_2 = browser.find_element(By.ID, "robotsRule")
    option_2.click()

    # Находим кнопку "Submit" и нажимаем ее
    button_1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_1.click()

finally:
    time.sleep(10)
    browser.quit()
