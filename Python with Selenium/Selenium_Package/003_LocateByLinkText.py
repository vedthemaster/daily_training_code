from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\\Users\\vedpa\\OneDrive\\Desktop\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://google.com")

driver.maximize_window()

# time.sleep(2)

i_element = driver.find_element_by_name("q")
# i_element = driver.find_element_by_id("lst-ib") 
i_element.send_keys("Techbeamers")
i_element.submit()

# time.sleep(3)
# f_element = driver.find_element_by_link_text("Python Tutorial")
f_element = driver.find_element_by_partial_link_text("Python")
f_element.click()