# Метод execute_script

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(num)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num_element = browser.find_element(By.ID, "input_value")
    num = num_element.text

    answer = calc(num)

    input_1 = browser.find_element(By.ID,"answer")
    input_1.send_keys(answer)

    footer = browser.find_element(By.CLASS_NAME, "bd-footer")
    # Элемент "footer" становится невидимым при помощи скрипта
    browser.execute_script("arguments[0].style.visibility = 'hidden'", footer)

    option_1 = browser.find_element(By.ID, "robotCheckbox")
    option_1.click()

    option_2 = browser.find_element(By.ID, "robotsRule")
    # Скролл до элемента "option_2" при помощи скрипта
    #browser.execute_script("return arguments[0].scrollIntoView(true);", option_2)
    option_2.click()

    button_1 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    # Скролл до элемента "button_1" при помощи скрипта
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button_1)
    button_1.click()

finally:
    time.sleep(5)
    browser.quit()
