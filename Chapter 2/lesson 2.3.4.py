# Окно alert

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(num)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button_1 = browser.find_element(By.CLASS_NAME, "btn-primary")
    button_1.click()

    # Делаем всплывающее окно активным элементом
    alert_1 = browser.switch_to.alert
    # Нажимаем "OK"
    alert_1.accept()
    # Или нажимаем "Отмена"
    #alert_1.dismiss()

    num_element = browser.find_element(By.ID, "input_value")
    num = num_element.text

    answer = calc(num)

    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(answer)

    button_2 = browser.find_element(By.CLASS_NAME, "btn-primary")
    button_2.click()

    # Делаем всплывающее окно активным элементом
    alert_2 = browser.switch_to.alert
    # Выводим на экран текст с ответом из всплывающего окна
    print(alert_2.text)

finally:
    browser.quit()
