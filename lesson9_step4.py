# Задание: принимаем alert
# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий
# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по #времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа на #это задание.

from selenium import webdriver
import time
import math
def calc(a):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    b = webdriver.Chrome()
    b.get('http://suninjuly.github.io/alert_accept.html')
    b.find_element_by_css_selector('.btn.btn-primary').click()
    confirm = b.switch_to.alert
    confirm.accept()
    #b.get('http://suninjuly.github.io/alert_redirect.html?')
    x = b.find_element_by_css_selector('#input_value').text
    b.find_element_by_css_selector('#answer').send_keys(calc(x))
    b.find_element_by_css_selector('[type="submit"]').click()
    alert = b.switch_to.alert
    alert_text = alert.text
    print(alert.text.split()[-1])
finally:
    time.sleep(5)
    b.quit()