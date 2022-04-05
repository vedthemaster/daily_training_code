import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\vedpa\\OneDrive\\Desktop\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/")

def login():
    login = driver.find_element(by=By.XPATH,value="""/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a""")
    login.click()
    email=driver.find_element(by=By.NAME,value="Email")
    email.send_keys("keyurkumar.patel9191@gmail.com")
    password=driver.find_element(by=By.ID,value="Password")
    password.send_keys("Keyur@91")
    time.sleep(2)
    driver.find_element(by=By.XPATH,value="""/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input""").click()
    

def search_product():
    product = driver.find_element(by=By.XPATH,value="/html/body/div[4]/div[1]/div[2]/ul[1]/li[4]/a")
    product.click()
    find = driver.find_element(by=By.ID,value="small-searchterms")
    find.send_keys("Jeans")
    serach=driver.find_element(by=By.XPATH,value="""/html/body/div[4]/div[1]/div[1]/div[3]/form/input[2]""")
    serach.click()
    select_product=driver.find_element(by=By.XPATH,value="""/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[3]/div[1]/div/div/div[1]/a/img""")
    select_product.click()

def add_to_cart():
    qty = driver.find_element(by=By.XPATH,value="""//*[@id="addtocart_36_EnteredQuantity"]""")
    qty.clear()

    enter_qty=driver.find_element(by=By.XPATH,value="""//*[@id="addtocart_36_EnteredQuantity"]""")
    enter_qty.send_keys("25")

    addtocart = driver.find_element(by=By.XPATH,value="""//*[@id="add-to-cart-button-36"]""")
    addtocart.click()
    gotocart = driver.find_element(by=By.XPATH,value="""//*[@id="topcartlink"]/a""")
    time.sleep(2)
    gotocart.click()

def process_to_checkout():
    coupon = driver.find_element(by=By.NAME,value="discountcouponcode")
    coupon.send_keys("AutomationDiscount2")
    done = driver.find_element(by=By.XPATH,value="""/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/div[2]/div[1]/div[1]/div[1]/div[3]/input[2]""")
    done.click()
    driver.implicitly_wait(5)
    a = driver.find_element(by=By.XPATH,value="""/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/div[2]/div[1]/div[1]/div[1]/div[4]""").text
    print(a)
    assert a == "The coupon code was applied"
    select_country = driver.find_element(by=By.XPATH,value="""//*[@id="CountryId"]""")
    select_country.send_keys("India")
    driver.find_element(by=By.ID,value="termsofservice").click()
    checkout = driver.find_element(by=By.ID,value="checkout")
    checkout.click()

def billing():
    address = driver.find_element(by=By.XPATH,value="""//*[@id="billing-buttons-container"]/input""")
    address.click()
    time.sleep(1)

    step2 = driver.find_element(by=By.XPATH,value="""//*[@id="shipping-buttons-container"]/input""")
    step2.click()
    time.sleep(1)

    nextdayprice = driver.find_element(by=By.XPATH,value="""//*[@id="checkout-shipping-method-load"]/div/div/ul/li[2]/div[1]/label""").text
    print(nextdayprice)
    assert nextdayprice == "Next Day Air (40.00)"

    step3 = driver.find_element(by=By.XPATH,value="""//*[@id="shippingoption_1"]""")
    step3.click()
    driver.find_element(by=By.XPATH,value="""//*[@id="shipping-method-buttons-container"]/input""").click()
    time.sleep(1)

    pay = driver.find_element(by=By.XPATH,value="""//*[@id="checkout-payment-method-load"]/div/div/ul/li[1]/div/div[2]/label""").text
    print(pay)
    assert pay =="Cash On Delivery (COD) (7.00)"

    cod = driver.find_element(by=By.XPATH,value="""//*[@id="paymentmethod_0"]""")
    cod.click()
    driver.find_element(by=By.XPATH,value="""//*[@id="payment-method-buttons-container"]/input""").click()
    time.sleep(1)
    driver.find_element(by=By.XPATH,value="""//*[@id="payment-info-buttons-container"]/input""").click()

    final_checkout = driver.find_element(by=By.XPATH, value="""//*[@id="confirm-order-buttons-container"]/input""")
    final_checkout.click()

def important_prints():
    driver.find_element(by=By.XPATH,value="""/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/ul/li[2]/a""").click()
    subtotal = driver.find_element(by=By.XPATH,value="""/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div[4]/table/tbody/tr[1]/td[2]/span""").text
    print("Total : ",subtotal)
    time.sleep(2)
    driver.find_element(by=By.XPATH,value="""/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a""").click()
    driver.find_element(by=By.XPATH,value="""/html/body/div[4]/div[1]/div[4]/div[1]/div/div[2]/ul/li[3]/a""").click()

def logout():
    time.sleep(2)
    order_id = driver.find_element(by=By.XPATH,value="""/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div/div[1]/div[1]/strong""").text
    print(order_id)
    logout = driver.find_element(by=By.XPATH,value="""/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a""")
    logout.click()


    
login()
search_product()
add_to_cart()
process_to_checkout()
billing()
important_prints()
logout()

