# Работа со списками (через click())

from selenium import webdriver
from selenium.webdriver.common.by import By
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

    selector_value = "option[value='" + answer + "']"

    # Находим элемент, раскрывающий список, и кликаем на него
    browser.find_element(By.ID, "dropdown").click()

    # Находим элемент, соответствующий значению "answer", и кликаем на него
    browser.find_element(By.CSS_SELECTOR, selector_value).click()

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    time.sleep(5)
    browser.quit()
