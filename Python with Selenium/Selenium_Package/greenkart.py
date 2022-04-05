from time import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(
    executable_path='C:\\Users\\vedpa\\OneDrive\\Desktop\\Drivers\\chromedriver_win32\\chromedriver.exe')

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()


search = driver.find_element(by=By.XPATH,value="//header/div[1]/div[2]/form[1]/input[1]")
search.send_keys("be")
time.sleep(3)

items = driver.find_elements(by=By.XPATH,value="//h4[@class='product-name']")
count = len(items)
# assert count == 3


for i in range(0,len(items)):
    print(items[i].text)

buttons = driver.find_elements(by=By.XPATH,value="//div[@class='product-action']/button")

for button in buttons:
    button.click()

bag = driver.find_element(by=By.XPATH,value="//header/div[1]/div[3]/a[4]/img[1]")
bag.click()

checkout = driver.find_element(by=By.XPATH,value="//button[contains(text(),'PROCEED TO CHECKOUT')]")
checkout.click()
time.sleep(2)

c_items = driver.find_elements(by=By.XPATH,value="//p[@class='product-name']")
count = len(c_items)
for i in range(0,len(c_items)):
    print(c_items[i].text)

amount =  driver.find_elements(by= By.XPATH,value="//p[@class='amount']")
print("amount lenght : ",len(amount))
f_amount=[]

for i in range(0,len(amount)):
    if(i%2 !=0):
        f_amount.append(int(amount[i].text))

print(sum(f_amount))

# print(f_amount[0])


# driver.find_element(by=By.XPATH,value="//button[contains(text(),'Place Order')]").click()

country = Select(driver.find_element(by=By.XPATH,value="//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/select[1]"))
country.select_by_visible_text("India")
driver.find_element(by=By.XPATH,value="//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/input[1]").click()

# wait =WebDriverWait(driver,4)
# wait.until(expected_conditions.presence_of_all_element_located((By.CLASS_NAME,"promoCode")))

driver.find_element(by=By.XPATH,value="//button[contains(text(),'Proceed')]").click()




