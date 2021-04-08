from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)
    find_x = browser.find_element_by_xpath('//*[@id="input_value"]')
    print(find_x.text)
    ans = browser.find_element_by_id('answer')
    i = calc(find_x.text)
    print(i)
    ans.send_keys(i)
    chek1 = browser.find_element_by_id('robotCheckbox')
    chek1.click()
    chek2 = browser.find_element_by_css_selector('[value="robots"]')
    chek2.click()
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()
    #Отметить checkbox "I'm the robot".
    #Выбрать radiobutton "Robots rule!".
    #Нажать на кнопку Submit.

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


Максим Курбанов
2 года назад
Ссылка
from selenium import webdriver
from math import log, sin

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")

x = browser.find_element_by_css_selector('[id = "input_value"]').text
browser.find_element_by_css_selector('[id = "answer"]').send_keys(str(log(abs(12 * sin(int(x))))))

for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', '.btn']:
    browser.find_element_by_css_selector(selector).click()