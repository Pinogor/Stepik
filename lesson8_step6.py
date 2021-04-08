from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/execute_script.html')
    a = browser.find_element_by_id('input_value').text
    print(calc(a))
    browser.find_element_by_css_selector('#answer').send_keys(calc(a))
    browser.find_element_by_css_selector('.form-check-label').click()
    scroll = browser.find_element_by_xpath('/html/body/div/form/div[4]/label')
    browser.execute_script("return arguments[0].scrollIntoView(true);", scroll)
    scroll.click()
    browser.find_element_by_css_selector('[type="submit"]').click()
    print_answer(browser)
finally:
    time.sleep(3)
    browser.quit()