from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    executable_path='C:\\Users\\vedpa\\OneDrive\\Desktop\\Drivers\\chromedriver_win32\\chromedriver.exe')

driver.get("https://login.salesforce.com")
driver.maximize_window()

driver.find_element(by =By.CSS_SELECTOR,value="#username").send_keys("teygfey")
driver.find_element(by =By.CSS_SELECTOR,value="#password").send_keys("fhdghfy")
driver.find_element(by=By.CSS_SELECTOR,value="#Login").click()

message = driver.find_element(by= By.XPATH,value="//div[@id='error']").text
print(message)
