
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):   # Base CLass will invoke driver and Fixture and other utilities
    # Another Test Case https://rahulshettyacademy.com/angularpractice/ form Submission

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage= HomePage(self.driver)
        log.info("first name is "+getData["firstname"])   # Write log
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()   # it will refresh browser else multiple data will be written within same field. pl comment and check

    # Create Class Variable to Access Data It is Dictionary only Key value Pair HomePageData.getTestData
    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))   # Parameterizing Tests using
                                                                    # data fixture with multiple Data Sets
    def getData(self, request):  # request return data - function with return value
        return request.param

