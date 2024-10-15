# Работа со списками (через Select)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element(By.ID, "num1")
    num1 = int(num1_element.text)

    num2_element = browser.find_element(By.ID, "num2")
    num2 = int(num2_element.text)

    answer = str(num1 + num2)

    # Инициализируем элемент, раскрывающий список, при помощи класса Select
    select = Select(browser.find_element(By.ID, "dropdown"))

    # Находим элемент, соответствующий значению "answer", и выделяем его
    select.select_by_value(answer)

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    time.sleep(5)
    browser.quit()
