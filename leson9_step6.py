# Задание: переход на новую вкладку
# В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.
#
# Сценарий для реализации выглядит так:
#
# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.

from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    b = webdriver.Chrome()
    b.get('http://suninjuly.github.io/redirect_accept.html')
    b.find_element_by_css_selector('.trollface.btn.btn-primary').click()
    new_win = b.window_handles[1]
    b.switch_to.window(new_win)
    b.find_element_by_css_selector('#answer').send_keys(calc(b.find_element_by_css_selector('#input_value').text))
    b.find_element_by_css_selector('[type="submit"]').click()
    alert = b.switch_to.alert
    alert_text = alert.text
    print(alert.text.split()[-1])

finally:
    time.sleep(0)
    b.quit()