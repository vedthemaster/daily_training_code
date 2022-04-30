
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(
    executable_path='C:\\Users\\vedpa\\OneDrive\\Desktop\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://www.goibibo.com/")
driver.maximize_window()

city = "Ahmedabad"
dcity = "Surat"

fromcity =driver.find_element(by=By.XPATH,value="//div[@class='sc-bkkeKt gAqCbJ fswFld ']/span[contains(text(),'From')]")
fromcity.click()
ecity =  driver.find_element(by=By.XPATH,value="//div[@class='sc-cidDSM dOEpbS']/input")
ecity.send_keys(city)

time.sleep(3)

foundcity = True
try:
    findc =driver.find_element(by=By.XPATH,value="//span[contains(text(),'"+city+", India')]")
    foundcity = True  
    driver.find_element(by=By.XPATH,value="//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]").click()
except NoSuchElementException:
    foundcity = False
    print("No City Found")
    
decity =  driver.find_element(by=By.XPATH,value="//div[@class='sc-cidDSM dOEpbS']/input")
decity.send_keys(dcity)
time.sleep(3)
try:
    findDcity = driver.find_element(by=By.XPATH,value="//span[contains(text(),'"+city+", India')]")
    foundcity=True
    driver.find_element(by=By.XPATH,value="//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[1]/div[1]").click()
except NoSuchElementException:
    foundcity = False
    print("No Second City Found")



    
    

