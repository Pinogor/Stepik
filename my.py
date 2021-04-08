from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.headless = True # Безголовый запуск
try:
    a=("[name='credit_sum']")
    browser = webdriver.Chrome(options = options)
    browser.implicitly_wait(5)
    browser.get('https://calcus.ru/kreditnyj-kalkulyator-s-dosrochnym-pogasheniem')
    browser.find_element_by_css_selector(a).send_keys('3700000')
    browser.find_element_by_css_selector("[name='period']").send_keys('30')
    browser.find_element_by_css_selector("[name='percent']").send_keys('7.2')
    browser.find_element_by_css_selector("[name='date_start']").send_keys('07-09-2020')
    browser.find_element_by_xpath('//div[1]/div[2]/div[1]/form/div[7]/div[2]/div/a').click()
    browser.find_element_by_xpath('//*[@id="addPaymentModal"]/div/div/form/div[1]/div[3]/div/div[1]/input').send_keys('12-10-2020')
    browser.find_element_by_xpath('//*[@id="addPaymentModal"]/div/div/form/div[1]/div[4]/div[2]/div[1]/div/input').send_keys('500000')
    select = Select(browser.find_element_by_xpath("//*[@id='addPaymentModal']/div/div/form/div[1]/div[5]/div[2]/div[1]/select"))
    select.select_by_value('2')
    browser.find_element_by_css_selector('.btn.btn-primary').click()
    browser.find_element_by_xpath('//div[1]/div[2]/div[1]/form/div[7]/div[2]/div/a').click()
    browser.find_element_by_xpath('//*[@id="addPaymentModal"]/div/div/form/div[1]/div[3]/div/div[1]/input').send_keys(
        '07-01-2021')
    browser.find_element_by_xpath(
        '//*[@id="addPaymentModal"]/div/div/form/div[1]/div[4]/div[2]/div[1]/div/input').send_keys('60000')
    select = Select(
        browser.find_element_by_xpath("//*[@id='addPaymentModal']/div/div/form/div[1]/div[5]/div[2]/div[1]/select"))
    select.select_by_value('2')

    browser.find_element_by_css_selector('.btn.btn-primary').click()
    browser.find_element_by_css_selector('.calc-submit').click()
    x = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/form/div[12]/div[1]")
    y = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[12]/div[2]/div')
    time.sleep(1.5)
    td = browser.find_element_by_css_selector('.result-placeholder-schedule').text
    print(td)
    data = open('data.txt', 'w')
    data.write(td)

finally:
    #time.sleep(9)
    browser.quit()