#Напишите код, который реализует следующий сценарий:
#Открыть страницу http://suninjuly.github.io/selects1.html
#Посчитать сумму заданных чисел
#Выбрать в выпадающем списке значение равное расчитанной сумме
#Нажать кнопку "Submit"
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')
    a = browser.find_element_by_id('num1').text
    b = browser.find_element_by_id('num2').text
    x = str((int(a) + int(b)))
    print(x)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(x)  # ищем элемент с текстом "Python"
    browser.find_element_by_css_selector('.btn').click()
    print_answer(browser)
finally:
    time.sleep(0)
    browser.quit()