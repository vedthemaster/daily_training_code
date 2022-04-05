
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome(
    executable_path='C:\\Users\\vedpa\\OneDrive\\Desktop\\Drivers\\chromedriver_win32\\chromedriver.exe')

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


a = ActionChains(driver)
m=driver.find_element(by=By.ID,value="mousehover")
a.move_to_element(m).perform()
time.sleep(3)

# driver.find_element(by=By.XPATH,value="//a[contains(text(),'Top')]").click
driver.find_element(by=By.XPATH,value="//a[contains(text(),'Reload')]").click


driver.find_element(by=By.XPATH,value="//input[@id='name']").send_keys("Test1")
driver.find_element(by=By.XPATH,value="//input[@id='alertbtn']").click()

time.sleep(2)
alert = Alert(driver)
print(alert.text)
alert.accept()

driver.find_element(by=By.XPATH,value="//input[@id='name']").send_keys("Test2")
driver.find_element(by=By.XPATH,value="//input[@id='confirmbtn']").click()
time.sleep(2)

print(alert.text)
alert.dismiss()


radio_list = driver.find_elements(by=By.NAME,value="radioButton")
time.sleep(1)

for b in radio_list:
    b.click()
    time.sleep(1)

driver.find_element(by= By.XPATH,value="//input[@id='autocomplete']").send_keys("ind")
time.sleep(1)
driver.find_element(by=By.XPATH,value="/html[1]/body[1]/ul[1]/li[2]/div[1]").click()


dropdown = Select(driver.find_element(by=By.XPATH,value="//select[@id='dropdown-class-example']"))
# dropdown.select_by_index(2)
# dropdown.select_by_value("option3")
dropdown.select_by_visible_text("Option1")

# dropdown.deselect_by_index(2)

driver.find_element(by=By.ID,value="checkBoxOption1").click()
driver.find_element(by=By.ID,value="checkBoxOption3").click()

table_rows =driver.find_elements(by=By.XPATH,value="//body/div[3]/div[1]/fieldset[1]/table[1]/tbody/tr")
table_col =driver.find_elements(by=By.XPATH,value="//body/div[3]/div[1]/fieldset[1]/table[1]/tbody/tr/th")
print(len(table_rows))
print(len(table_col))

print(table_rows[2].text)
print(table_col[2].text)


