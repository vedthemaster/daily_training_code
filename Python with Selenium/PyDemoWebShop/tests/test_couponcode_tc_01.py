import time
from utilities.BaseClass import BaseClass
from TestData.commonData import CommonData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class TestCase01(BaseClass):
    
    def test_couponcode(self):
        
        log = self.getLogger()
        self.loginToCart();
        # self.emptyCart()
        
        coupon = self.driver.find_element(by=By.NAME, value="discountcouponcode")
        coupon.send_keys(CommonData.coupon1)
        done = self.driver.find_element(by=By.XPATH, value="""/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/div[2]/div[1]/div[1]/div[1]/div[3]/input[2]""")
        done.click()
        self.driver.implicitly_wait(5)
        a = self.driver.find_element(by=By.XPATH, value="""/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/div[2]/div[1]/div[1]/div[1]/div[4]""").text
        print(a)
        assert a == "The coupon code was applied"
        select_country = self.driver.find_element(by=By.XPATH, value="""//*[@id="CountryId"]""")
        select_country.send_keys("India")
        self.driver.find_element(by=By.ID, value="termsofservice").click()
        checkout = self.driver.find_element(by=By.ID, value="checkout")
        checkout.click()
        log.info("Proceed to checkout Successful")
        
        address = self.driver.find_element(by=By.XPATH, value="""//*[@id="billing-buttons-container"]/input""")
        address.click()
        time.sleep(1)

        step2 = self.driver.find_element(by=By.XPATH, value="""//*[@id="shipping-buttons-container"]/input""")
        step2.click()
        time.sleep(1)

        nextdayprice = self.driver.find_element(by=By.XPATH, value="""//*[@id="checkout-shipping-method-load"]/div/div/ul/li[2]/div[1]/label""").text
        print(nextdayprice)
        
        step3 = self.driver.find_element(by=By.XPATH, value="""//*[@id="shippingoption_1"]""")
        step3.click()
        self.driver.find_element(by=By.XPATH, value="""//*[@id="shipping-method-buttons-container"]/input""").click()
        time.sleep(1)
        
        cd = self.driver.find_element(by=By.ID, value="paymentmethod_2")
        cd.click()
        
        self.driver.find_element(by=By.XPATH, value="""//*[@id="payment-method-buttons-container"]/input""").click()
        time.sleep(1)

        CardType = Select(self.driver.find_element(by=By.ID, value="CreditCardType"))
        CardType.select_by_visible_text(CommonData.ccType)
        time.sleep(2)

        CardName = self.driver.find_element(by=By.ID, value="CardholderName")
        CardName.send_keys(CommonData.ccName)
        time.sleep(2)

        CardNumber = self.driver.find_element(by=By.ID, value="CardNumber")
        CardNumber.send_keys(CommonData.ccNumber)
        time.sleep(2)

        ExpireMonth = Select(self.driver.find_element(by=By.ID, value="ExpireMonth"))
        ExpireMonth.select_by_index(CommonData.ccMonth-1)
        time.sleep(2)

        ExpireYear = Select(self.driver.find_element(by=By.ID, value="ExpireYear"))
        ExpireYear.select_by_visible_text(str(CommonData.ccYear))
        time.sleep(2)

        CardCode = self.driver.find_element(by=By.ID, value="CardCode")
        CardCode.send_keys(CommonData.cvv)
        time.sleep(2)

        self.driver.find_element(by=By.XPATH, value="""//*[@id="payment-info-buttons-container"]/input""").click()
        final_checkout = self.driver.find_element(by=By.XPATH, value="""//*[@id="confirm-order-buttons-container"]/input""")
        final_checkout.click()

        log.info("Billing Process using Credit card Successful")
        
        self.driver.find_element(by=By.XPATH, value="""/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/ul/li[2]/a""").click()
        subtotal = self.driver.find_element(by=By.XPATH, value="""/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div[4]/table/tbody/tr[1]/td[2]/span""").text
        print("Sub Total : ", subtotal)
        time.sleep(2)

        shippingcost = self.driver.find_element(By.XPATH,"//span[contains(text(),'40.00')]").text
        print("Shipping cost:",shippingcost)

        GrandTotal = (float(subtotal) + float(shippingcost)) - 13.00
        print(GrandTotal)
        
        self.driver.find_element(by=By.XPATH, value="""/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a""").click()
        self.driver.find_element(by=By.XPATH, value="""/html/body/div[4]/div[1]/div[4]/div[1]/div/div[2]/ul/li[3]/a""").click()

        log.info("Important Prints Successful")  # Write log

        #Logout

        time.sleep(2)
        order_id = self.driver.find_element(by=By.XPATH, value="""/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div/div[1]/div[1]/strong""").text
        print(order_id)
        logout = self.driver.find_element(by=By.XPATH, value="""/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a""")
        logout.click()
        log.info("Logout Successful")  # Write log
        print("Logout Successfully Done")

        
        
        
        