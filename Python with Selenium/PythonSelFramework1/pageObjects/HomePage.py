from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage

# Here idea as
# Declare one Page Object, one locator within two arguments in a tuple location and actual locator
# and locator type and you just called that in your method and you will return

class HomePage:

    def __init__(self, driver):   # send driver as argument else empty constructor will be created
        self.driver = driver      # to pass driver object create constructor
                                  # Sending Actual Class driver local driver
    shop = (By.CSS_SELECTOR, "a[href*='shop']")  # Tuple
    # 1 driver.find_element_by_css_selector("a[href*='shop']")
    # Instance variable can be accessed by using Self.variable_name
    # constructor variable or class can be accessed with class.variable_name

    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender= (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()     # * meant it will consider as tuple desirealise
        checkOutPage = CheckOutPage(self.driver)              #.click is Smarter way of returning Page objects
                                                                # from Navigation Method
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)


    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)




