from selenium import webdriver
b = webdriver.Chrome()
b.implicitly_wait(5) #Ожиданиепоиска элемента для всего кода
b.get('http://suninjuly.github.io/cats.html')
try:
    b.find_element_by_id("button")
finally:
    b.quit()