# Метод get_attribute()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(num):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    chest_element = browser.find_element(By.ID, "treasure")
    x = chest_element.get_attribute("valuex")
    answer = calc(x)

    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(answer)

    option_1 = browser.find_element(By.ID, "robotCheckbox")
    option_1.click()

    option_2 = browser.find_element(By.ID, "robotsRule")
    option_2.click()

    button_1 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_1.click()

finally:
    time.sleep(10)
    browser.quit()
