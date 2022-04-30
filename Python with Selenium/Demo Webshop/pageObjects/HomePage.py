from selenium.webdriver.common.by import By



class HomePage:
    def __init__(self,driver):
        self.driver = driver
        
        register = (By.XPATH,"//a[contains(text(),'Register')]")
        login = (By.XPATH,"//a[contains(text(),'Log in')]")
        shoppingcart = (By.XPATH,"//span[contains(text(),'Shopping cart')]")
        wishlist = (By.XPATH,"//span[contains(text(),'Wishlist')]")
        myaccount = (By.CSS_SELECTOR,"a[class=account]")
        logout = (By.XPATH,"//a[contains(text(),'Log out')]")
        shoes = (By.LINK_TEXT,"Apparel & Shoes")
        
        def gotoRegister(self):
            return self.driver.find_element(*HomePage.register)
        
        def gotoLogin(self):
            return self.driver.find_element(*HomePage.login)
        
        def gotoCart(self):
            return self.driver.find_element(*HomePage.shoppingcart)
        
        def gotoWishList(self):
            return self.driver.find_element(*HomePage.wishlist)
        
        def gotoMyAccount(self):
            return self.driver.find_element(*HomePage.myaccount)
        
        def gotoLogOut(self):
            return self.driver.find_element(*HomePage.logout)
        
        def gotoShoes(self):
            return self.driver.find_element(*HomePage.shoes)
            
        
        
                        
            
    