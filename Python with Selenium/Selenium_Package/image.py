from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    executable_path='C:\\Users\\vedpa\\OneDrive\\Desktop\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("http://demowebshop.tricentis.com/login")

driver.find_element(by=By.XPATH,value="//body/div[4]/div[1]/div[1]/div[1]/a[1]/img[1]").click()

links = driver.find_elements(by=By.TAG_NAME,value="a")
print("test")
print(len(links))
print()