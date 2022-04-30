import time

from selenium import webdriver
from selenium.webdriver.common.by import By

month_year = 'August 2022'
u_date = 9
u_date = str(u_date)
print(u_date)
driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.makemytrip.com/")
driver.find_element(By.XPATH, "//*[@id='SW']/div[1]/div[1]/ul/li[3]").click()
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[3]/label/span").click()
time.sleep(1)
page_month_year = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div").text
while page_month_year != month_year:
    page_month_year = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[3]/div["
                                                    "1]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div").text
    print(page_month_year)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div["
                                  "2]/div/div[1]/span[2]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//div[@class='DayPicker-Month']//div[@class='dateInnerCell']//p[1][contains(text(),'"+u_date+"')]").click()