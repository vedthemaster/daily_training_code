from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(
    executable_path='C:\\Users\\vedpa\\OneDrive\\Desktop\\Drivers\\chromedriver_win32\\chromedriver.exe')

driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")
driver.find_element(by=By.CSS_SELECTOR,value="#tinymce").clear()
driver.find_element(by=By.CSS_SELECTOR,value="#tinymce").send_keys("This is automated")
driver.switch_to.default_content()
print(driver.find_element(by=By.TAG_NAME,value="h3").text)
