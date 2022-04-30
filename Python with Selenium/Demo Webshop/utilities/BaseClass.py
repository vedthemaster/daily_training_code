import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from pageObjects.HomePage import HomePage
import time


# Base class
# Define utilities here which are used across multiple test cases
# like logging, reporting, fixtures
# Also you can write common functions here like verifyLinkPresence(Just Pass Object and Text)
# eg. selectOptionByText, you can write control specific methods here/ general methods for
# each control
#

@pytest.mark.usefixtures("setup")  # 1 Add setup Fixture as this Fixture is common for each
# test case
# you can access methods of fixtures into BaseClass
class BaseClass:
# Logger Utility is used to create log along with inspect, file handler and Formatter
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text): # This method is used to verify that
                                        # particular link is present or not
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self,locator,text):   # This method is used to select Gender
        sel = Select(locator)
        sel.select_by_visible_text(text)
        
    def emptyCart(self):
        
        (HomePage.driver).gotoCart.click()
        cartitems = self.driver.find_elements(By.CSS_SELECTOR,"input[name=removefromcart]")
        
        for item in len(cartitems):
            item.click()
        self.driver.find_element(By.CSS_SELECTOR,"input[name=updatecart]").click()
        
    def loginToCart(self):
        log = self.getLogger();
        (HomePage.driver).gotoLogin.click()
        
        email = self.driver.find_element(by=By.NAME, value="Email")
        email.send_keys("keyurkumar.patel9191@gmail.com")
        password = self.driver.find_element(by=By.ID, value="Password")
        password.send_keys("Keyur@91")
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value="""/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input""").click()

        # loginPage = topMenu.login()
        log.info("Login Successful")  # Write log
        
        pMenu = self.driver.find_element(by=By.PARTIAL_LINK_TEXT,value="Apparel & Sho")
        pMenu.click()
        
        find = self.driver.find_element(by=By.ID, value="small-searchterms")
        find.send_keys("Jeans")
        search = self.driver.find_element(by=By.XPATH, value="""/html/body/div[4]/div[1]/div[1]/div[3]/form/input[2]""")
        search.click()
        select_product = self.driver.find_element(by=By.XPATH, value="""/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[3]/div[1]/div/div/div[1]/a/img""")
        select_product.click()
        qty = self.driver.find_element(by=By.XPATH, value="""//*[@id="addtocart_36_EnteredQuantity"]""")
        qty.clear()

        enter_qty = self.driver.find_element(by=By.XPATH, value="""//*[@id="addtocart_36_EnteredQuantity"]""")
        enter_qty.send_keys("25")
        
        addtocart = self.driver.find_element(by=By.XPATH, value="""//*[@id="add-to-cart-button-36"]""")
        addtocart.click()
        gotocart = self.driver.find_element(by=By.XPATH, value="""//*[@id="topcartlink"]/a""")
        time.sleep(2)
        gotocart.click()
        log.info("Add to cart Successful")  # Write log
        

        
        
        
            
        
        
