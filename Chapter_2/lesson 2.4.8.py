# Ожидания (явные и неявные)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.wait import WebDriverWait
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    # Указываем ждать все элементы в течение 5 секунд (с постоянной проверкой через каждые 500 мс)
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Указываем проверять в течение 12 секунд, пока цена не станет равна "$100"
    price = WebDriverWait(browser, 12).until(text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element(By.ID, "book")
    button.click()

    num_element = browser.find_element(By.ID, "input_value")
    num = num_element.text

    answer = calc(num)

    input_1 = browser.find_element(By.ID,"answer")
    input_1.send_keys(answer)

    button = browser.find_element(By.ID, "solve")
    button.click()

    alert = browser.switch_to.alert
    print(alert.text)

finally:
    browser.quit()
