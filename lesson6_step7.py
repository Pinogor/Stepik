from selenium import webdriver
import time
link = "http://suninjuly.github.io/registration1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_xpath("//div[1]/div[1]/input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//div[1]/div[2]/input')
    input2.send_keys('Ivanov')
    input3 = browser.find_element_by_xpath('//div[1]/div[3]/input')
    input3.send_keys("ghjgjvh@gml.ru")
    button = browser.find_element_by_xpath('//div/form/button')
    button.click()
finally:
    time.sleep(6)
    browser.quit()

