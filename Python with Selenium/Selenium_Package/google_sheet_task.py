from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
    executable_path='C:\\Users\\vedpa\\OneDrive\\Desktop\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://docs.google.com/spreadsheets/")

driver.maximize_window()


driver.find_element_by_xpath('//*[@id ="identifierId"]').send_keys("your email")
driver.find_element_by_class_name("VfPpkd-vQzf8d").click()
driver.implicitly_wait(3)

driver.find_element_by_name("password").send_keys("your password")
driver.find_element_by_id("passwordNext").click()

driver.find_element_by_xpath("//body/div[4]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/img[1]").click()
driver.find_element_by_xpath("//body/div[@id='docs-chrome']/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]").clear()
driver.find_element_by_xpath("//body/div[@id='docs-chrome']/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]").send_keys("Sheet by automation")
driver.find_element_by_xpath("//body/div[@id='docs-chrome']/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]").send_keys(Keys.ENTER)



driver.find_element_by_xpath("/html[1]/body[1]/div[9]/div[1]/div[1]").send_keys("Name")
driver.find_element_by_xpath("/html[1]/body[1]/div[9]/div[1]/div[1]").send_keys(Keys.TAB)

driver.find_element_by_xpath("/html[1]/body[1]/div[9]/div[1]/div[1]").send_keys("Age")
driver.find_element_by_xpath("/html[1]/body[1]/div[9]/div[1]/div[1]").send_keys(Keys.ENTER)

driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[9]/div[6]/div[1]/input[1]").clear()
driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[9]/div[6]/div[1]/input[1]").send_keys("A2")
driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[9]/div[6]/div[1]/input[1]").send_keys(Keys.ENTER)

driver.find_element_by_xpath("/html[1]/body[1]/div[9]/div[1]/div[1]").send_keys("Ved")
driver.find_element_by_xpath("/html[1]/body[1]/div[9]/div[1]/div[1]").send_keys(Keys.TAB)
driver.find_element_by_xpath("/html[1]/body[1]/div[9]/div[1]/div[1]").send_keys("21")
driver.find_element_by_xpath("/html[1]/body[1]/div[9]/div[1]/div[1]").send_keys(Keys.ENTER)

driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[9]/div[6]/div[1]/input[1]").clear()
driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[9]/div[6]/div[1]/input[1]").send_keys("A3")
driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[9]/div[6]/div[1]/input[1]").send_keys(Keys.ENTER)

driver.find_element_by_xpath("/html[1]/body[1]/div[9]/div[1]/div[1]").send_keys("Keyur")
driver.find_element_by_xpath("/html[1]/body[1]/div[9]/div[1]/div[1]").send_keys(Keys.TAB)
driver.find_element_by_xpath("/html[1]/body[1]/div[9]/div[1]/div[1]").send_keys("20")
driver.find_element_by_xpath("/html[1]/body[1]/div[9]/div[1]/div[1]").send_keys(Keys.ENTER)

driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[9]/div[6]/div[1]/input[1]").clear()
driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[9]/div[6]/div[1]/input[1]").send_keys("A4")
driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[9]/div[6]/div[1]/input[1]").send_keys(Keys.ENTER)

driver.find_element_by_xpath("/html[1]/body[1]/div[9]/div[1]/div[1]").send_keys("Kushang")
driver.find_element_by_xpath("/html[1]/body[1]/div[9]/div[1]/div[1]").send_keys(Keys.TAB)
driver.find_element_by_xpath("/html[1]/body[1]/div[9]/div[1]/div[1]").send_keys("21")
driver.find_element_by_xpath("/html[1]/body[1]/div[9]/div[1]/div[1]").send_keys(Keys.ENTER)