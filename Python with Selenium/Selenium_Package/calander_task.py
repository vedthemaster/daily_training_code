
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(
    executable_path='C:\\Users\\vedpa\\OneDrive\\Desktop\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://www.expedia.co.in/")

driver.find_element(by=By.XPATH,value="//button[@id='d1-btn']").click()
driver.find_element(by=By.XPATH,value="//button[@aria-label='11 May 2022']").click()

# uDate = input("Enter a date: ")
# uMonth = input("Enter a Month: ")


nextb = driver.find_element(by= By.XPATH,value="//body/div[@id='app-blossom-flex-ui']/div[@id='app-layer-manager']/div[@id='app-layer-base']/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/button[2]")


def moncheck(uMonth,checktext):  
    checktext = driver.find_elements(by=By.XPATH,value="//div[@data-stid='date-picker-month']/h2")
    fchecktxt =[]
    for tet in checktext:
        fchecktxt.append(tet.text)
    while(uMonth in fchecktxt):
        driver.find_element(by=By.XPATH,value="//button[@aria-label='11 Apr 2022']").click()
    else:
        nextb.click()
        checktext = driver.find_elements(by=By.XPATH,value="//div[@data-stid='date-picker-month']/h2").text
    
    
# print(checktext)

