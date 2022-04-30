from selenium.webdriver.common.by import By



class HomePage:
    # def __init__(self,driver):
    #     self.driver = driver
        
    #     register = (By.XPATH,"//a[contains(text(),'Register')]")
    #     login = (By.XPATH,"//a[contains(text(),'Log in')]")
    #     shoppingcart = (By.XPATH,"//span[contains(text(),'Shopping cart')]")
    #     wishlist = (By.XPATH,"//span[contains(text(),'Wishlist')]")
    #     myaccount = (By.CSS_SELECTOR,"a[class=account]")
    #     logout = (By.XPATH,"//a[contains(text(),'Log out')]")
    #     shoes = (By.LINK_TEXT,"Apparel & Shoes")
        
    #     def gotoRegister(self):
    #         self.driver.find_element(*HomePage.register).click()
        
    #     def gotoLogin(self):
    #         self.driver.find_element(*HomePage.login).click()
        
    #     def gotoCart(self):
    #         self.driver.find_element(*HomePage.shoppingcart).click()
        
    #     def gotoWishList(self):
    #         self.driver.find_element(*HomePage.wishlist).click()
        
    #     def gotoMyAccount(self):
    #         self.driver.find_element(*HomePage.myaccount).click()
        
    #     def gotoLogOut(self):
    #         return self.driver.find_element(*HomePage.logout).click()
        
    #     def gotoShoes(self):
    #         self.driver.find_element(*HomePage.shoes).click()
    
    def __init__(self, driver):     # send driver as argument else empty constructor will be created
        self.driver = driver        # to pass driver object create constructor

    # register = (By.CSS_SELECTOR,".ico-register")
    register = (By.XPATH,"//a[contains(text(),'Register')]")
    login = (By.XPATH,"//a[contains(text(),'Log in')]")
    shoppingcart = (By.XPATH,"//span[contains(text(),'Shopping cart')]")    
    wishlist = (By.XPATH,"//span[contains(text(),'Wishlist')]")
    logout = (By.XPATH,"//a[contains(text(),'Log out')]")
    myaccount = (By.CSS_SELECTOR,"a[class=account]")
    

    #TopMenu Declaration...
    def loginClick(self):
        self.driver.find_element(*HomePage.login).click()
    def shoppingCartClick(self):
        self.driver.find_element(*HomePage.shoppingcart).click()
    def wishListClick(self):
        self.driver.find_element(*HomePage.wishlist).click()
    def logOutClick(self):
        self.driver.find_element(*HomePage.logout).click()
    def myaccountClick(self):
        self.driver.find_element(*HomePage.myaccount).click()
    
            
        
        
                        
            
    