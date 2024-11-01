from asyncio import timeout

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(60)
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestStepic:



    links1 = ["https://stepik.org/lesson/236895/step/1"]

    links = ["https://stepik.org/lesson/236895/step/1",
            "https://stepik.org/lesson/236896/step/1",
            "https://stepik.org/lesson/236897/step/1",
            "https://stepik.org/lesson/236898/step/1",
            "https://stepik.org/lesson/236899/step/1",
            "https://stepik.org/lesson/236903/step/1",
            "https://stepik.org/lesson/236904/step/1",
            "https://stepik.org/lesson/236905/step/1"]

    # Указываем параметр для подстановки в тест и что именно подставлять
    @pytest.mark.parametrize('link', links)
    def test_user_can_login(self, browser, link):

        login = 'dartie@mail.ru'
        password = '1234567890'

        answer = math.log(int(time.time()))

        browser.get(link)

        # Кликаем по кнопке "Войти"
        button_1 = WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "navbar__auth_login")))
        button_1.click()

        # Вводим логин
        input_1 = browser.find_element(By.ID, "id_login_email")
        input_1.send_keys(login)

        # Вводим пароль
        input_2 = browser.find_element(By.ID, "id_login_password")
        input_2.send_keys(password)

        # Кликаем по кнопке "Войти"
        button_2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
        button_2.click()

        # Кликаем по кнопке "Сброс"
        #button_4 = browser.find_element(By.CLASS_NAME, "again-btn white")
        #button_4.click()

        # Вводим ответ
        input_3 = WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "ember-text-area")))
        input_3.send_keys(answer)

        time.sleep(5)
        
        # Кликаем по кнопке "Отправить"
        button_3 = WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "submit-submission")))
        button_3.click()

        time.sleep(5)

        # Проверяем соответствие текста
        message = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
        #message = WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
        message_check = message.text
        print(message_check)
        assert "Correct!" == message_check, \
                f"expected 'Correct!', got {message_check}"