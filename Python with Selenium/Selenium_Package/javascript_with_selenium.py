
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(
    executable_path='C:\\Users\\vedpa\\OneDrive\\Desktop\\Drivers\\chromedriver_win32\\chromedriver.exe')


driver.get("https://rahulshettyacademy.com/angularpractice")

driver.find_element(by=By.XPATH,value="//body/app-root[1]/form-comp[1]/div[1]/form[1]/div[1]/input[1]").send_keys("Ved")
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

