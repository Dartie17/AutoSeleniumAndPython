import pytest
from selenium import webdriver

# Добавляем параметр запуска тестов в командной строке(чем запускать - хромом или фаерфоксом). Можно задать значение по умолчанию
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrome or firefox")

# Запуск браузера
@pytest.fixture(scope="function")
def browser(request):
    # Получаем параметр командной строки browser_name
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()