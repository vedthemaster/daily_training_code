from email import message
from selenium import webdriver
from selenium.webdriver.support.select import Select
from datetime import datetime


driver = webdriver.Chrome(executable_path='C:\\Users\\vedpa\\OneDrive\\Desktop\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("Ved")
driver.find_element_by_name("email").send_keys("ved@mail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("ThisIsPassword")
driver.find_element_by_id("inlineRadio2").click()
driver.find_element_by_name("bday").send_keys("03032001")

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
# dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)


driver.find_element_by_class_name("btn").click()
s_message = driver.find_element_by_class_name("alert-success").text

c_now = datetime.now()
filename1 = "ss"+ c_now.strftime("%m/%d/%Y%H:%M:%S")+".png"
print(filename1)
# driver.get_screenshot_as_file()
