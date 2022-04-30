import imp
from lib2to3.pgen2 import driver
from attr import validate
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(
    executable_path='C:\\Users\\vedpa\\OneDrive\\Desktop\\Drivers\\chromedriver_win32\\chromedriver.exe')

def fileupload():
    driver.get("https://images.google.com/")

    driver.find_element(by=By.XPATH,value="//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/span[1]").click()
    time.sleep(1)
    driver.find_element(by=By.LINK_TEXT,value="Upload an image").click()
    f_upload = driver.find_element(by=By.XPATH,value="//input[@id='awyMjb']")
    f_upload.send_keys("C:\\Users\\vedpa\\Downloads\\MicrosoftTeams-image.png")
    
fileupload()

def filedownload():
    driver.get("http://demo.automationtesting.in/FileDownload.html")
    driver.find_element(by=By.XPATH,value="//body/section[1]/div[1]/div[1]/div[1]/div[1]/a[1]").click()
filedownload()

