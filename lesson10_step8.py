# Задание: ждем нужный текст на странице
# Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.
#
# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
#
# Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание.
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
#b.implicitly_wait(5)
b = webdriver.Chrome()
try:
    b.get('http://suninjuly.github.io/explicit_wait2.html')
    WebDriverWait(b, 10).until(EC.text_to_be_present_in_element((By.ID, 'price'),'$100'))
    b.find_element_by_css_selector('#book').click()
    b.execute_script("window.scrollBy(0,100);")
    b.find_element_by_css_selector('#answer').send_keys(calc(b.find_element_by_css_selector('#input_value').text))
    b.find_element_by_css_selector('#solve').click()
    alert = b.switch_to.alert
    print(alert.text.split()[-1])

finally:
    time.sleep(5)
    b.quit()