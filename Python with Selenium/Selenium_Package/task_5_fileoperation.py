from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(
    executable_path='C:\\Users\\vedpa\\OneDrive\\Desktop\\Drivers\\chromedriver_win32\\chromedriver.exe')

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

driver.find_element(by=By.XPATH,value="//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]").click()


