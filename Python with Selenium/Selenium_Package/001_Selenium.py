from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Users\\vedpa\\OneDrive\\Desktop\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://demo.opencart.com/")
driver.maximize_window()

print("This is title" + driver.title)
print("Current URL" + driver.current_url)
driver.get("https://demo.opencart.com/index.php?route=account/login")

# driver.back()
# driver.refresh()
# driver.close()
# driver.quit()


