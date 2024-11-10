from selenium.webdriver.common.by import By
import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestBasket:

    def test_basket_button_is_on_page(self, browser):

        browser.get(link)
        browser.implicitly_wait(10)
        button = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')

        assert button, 'Кнопка добавления товара в корзину отсутствует'