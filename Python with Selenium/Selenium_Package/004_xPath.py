from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Users\\vedpa\\OneDrive\\Desktop\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://demo.opencart.com/")

driver.find_element_by_xpath("//header/div[1]/div[1]/div[2]/div[1]/input[1]").send_keys("Mac")
driver.find_element_by_xpath("//header/div[1]/div[1]/div[2]/div[1]/span[1]/button[1]").click() 