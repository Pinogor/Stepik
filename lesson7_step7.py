#Открыть страницу http://suninjuly.github.io/get_attribute.html.
#Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
#Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
#Посчитать математическую функцию от x (сама функция остаётся неизменной).
#Ввести ответ в текстовое поле.
#Отметить checkbox "I'm the robot".
#Выбрать radiobutton "Robots rule!".
#Нажать на кнопку "Submit".
#Для вычисления значения выражения в п.4 используйте функцию calc(x) из предыдущей задачи.
#Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Скопируйте его в поле ниже и нажмите кнопку "Submit", чтобы получить баллы за задание.
from selenium import webdriver
import time
import math
def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')
    box = browser.find_element_by_id('treasure')
    valuex = box.get_attribute('valuex')
    print(valuex)
    browser.find_element_by_id('answer').send_keys(calc(valuex))
    print(calc(valuex))
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector('.btn').click()
    print_answer(browser)
finally:
    time.sleep(0)
    browser.quit()
