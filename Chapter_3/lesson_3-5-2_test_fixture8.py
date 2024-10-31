# Маркировка
# pytest -s -v -m smoke filename.py    Запуск тестов с указанной меткой
# pytest -s -v -m "not smoke" filename.py    Запуск всех тестов, кроме указанной метки
# pytest -s -v -m "smoke or regression" filename.py    Запуск тестов, имеющих первую или вторую метку
# pytest -s -v -m "smoke and win10" filename.py    Запуск тестов, имеющих обе метки сразу

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    # Задаем метку для теста
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    # Задаем метку для теста
    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")