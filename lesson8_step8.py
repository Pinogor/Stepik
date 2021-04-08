#!/media/user/lin/download/selenium-3.141.0
#!/usr/local/bin/chromedriver
#Задание: загрузка файла
#В этом задании в форме регистрации требуется загрузить текстовый файл.
#Напишите скрипт, который будет выполнять следующий сценарий:
#Открыть страницу http://suninjuly.github.io/file_input.html
#Заполнить текстовые поля: имя, фамилия, email
#Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
#Нажать кнопку "Submit"
#Если все сделано правильно и быстро, вы увидите окно с числом. Отправьте полученное #число в качестве ответа для этого задания.
from selenium import webdriver
import os
import time
def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
try:
    b = webdriver.Chrome('/usr/local/bin/chromedriver')
    a = os.path.abspath(__file__)
    b.get('http://suninjuly.github.io/file_input.html')
    b.find_element_by_css_selector('[name="firstname"]').send_keys('Ivan')
    b.find_element_by_css_selector('[name="lastname"]').send_keys('Ivanov')
    b.find_element_by_css_selector('[name="email"]').send_keys('ivanov@mail.ru')
    b.find_element_by_css_selector('#file').send_keys(a)
    b.find_element_by_css_selector('.btn.btn-primary').click()
    print_answer(b)
finally:
    time.sleep(3)
    b.quit()