from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    executable_path='C:\\Users\\vedpa\\OneDrive\\Desktop\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://www.makemytrip.com/")
time.sleep(2)

driver.find_element(by=By.CSS_SELECTOR, value="span[class='langCardClose']").click()

driver.find_element(by=By.CSS_SELECTOR,
                    value="li[class='makeFlex hrtlCenter font10 makeRelative lhUser userLoggedOut']").click()

driver.find_element(by=By.CSS_SELECTOR, value="div[class='fsw_inputBox dates inactiveWidget ']").click()
time.sleep(2)
driver.find_element(by=By.CSS_SELECTOR, value="div[aria-label='Wed Apr 06 2022']").click()
time.sleep(1)
driver.find_element(by=By.CSS_SELECTOR, value="div[class='fsw_inputBox dates reDates inactiveWidget ']").click()
time.sleep(1)
driver.find_element(by=By.CSS_SELECTOR, value="div[aria-label='Sun Apr 10 2022']").click()

time.sleep(5)