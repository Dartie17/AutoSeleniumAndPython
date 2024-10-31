from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1:

    # Запускается один раз
    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite.. 1")
        self.browser = webdriver.Chrome()

    # Запускается один раз
    @classmethod
    def teardown_class(self):
        print("quit browser for test suite.. 1")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print("start test 1.1")
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print("start test 1.2")
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2:

    # Запускается перед каждым тестом
    def setup_method(self):
        print("start browser for test.. 2")
        self.browser = webdriver.Chrome()

    # Запускается перед каждым тестом
    def teardown_method(self):
        print("quit browser for test.. 2")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print("start test 2.1")
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print("start test 2.2")
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")