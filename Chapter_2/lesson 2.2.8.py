# Загрузка файлов

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input_1.send_keys("Ivan")

    input_2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input_2.send_keys("Ivanov")

    input_3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input_3.send_keys("ivanov@test.ru")

    # Создаем тестовый файл
    with open("file_example.txt", "w") as file:
        content = file.write("text_example")

    # Получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname('__file__'))

    # Добавляем к этому пути имя тестового файла
    file_path = os.path.join(current_dir, 'file_example.txt')

    # Находим кнопку загрузки файла
    upload_button = browser.find_element(By.ID, "file")

    # Передаем кнопке загрузки полный путь до тестового файла
    upload_button.send_keys(file_path)

    # Удаляем тестовый файл
    os.remove(file_path)

    button_1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_1.click()

finally:
    time.sleep(5)
    browser.quit()
