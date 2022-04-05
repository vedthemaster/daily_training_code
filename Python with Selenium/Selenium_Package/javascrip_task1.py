import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(
    executable_path='C:\\Users\\vedpa\\OneDrive\\Desktop\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://the-internet.herokuapp.com/nested_frames")




frametop = driver.find_element(by=By.NAME,value="frame-top")
driver.switch_to.frame(frametop)

frameleft = driver.find_element(by=By.NAME,value="frame-left")
driver.switch_to.frame(frameleft)
driver.execute_script('document.getElementsByTagName("body")[0].innerHTML = "This is left"')
# driver.execute_script('arguments[0].innerHTML=arguments[1]',b,wholepage),
time.sleep(2)

driver.switch_to.parent_frame()
frameright = driver.find_element(by=
By.NAME,value="frame-right")
driver.switch_to.frame(frameright)
driver.execute_script('document.getElementsByTagName("body")[0].innerHTML = "This is changed right"')
time.sleep(2)

driver.switch_to.parent_frame()

framemiddle = driver.find_element(by=By.NAME,value="frame-middle")
driver.switch_to.frame(framemiddle)
driver.execute_script('document.getElementsByTagName("body")[0].innerHTML = "This is changed middle"')
time.sleep(2)

driver.switch_to.parent_frame()

frameleft = driver.find_element(by=By.NAME,value="frame-left")
driver.switch_to.frame(frameleft)
wholepage = "<iframe src='https://the-internet.herokuapp.com/nested_frames'> </iframe>"
driver.execute_script('document.getElementsByTagName("body")[0].innerHTML = arguments[0]',wholepage)