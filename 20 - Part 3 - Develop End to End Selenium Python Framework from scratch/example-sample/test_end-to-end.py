import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from BaseClass import BaseClass
from HomePage import HomePage 
from CheckoutPage import CheckoutPage 


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):

        log = self.getlogger()

        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info("getting all card titles")

        products = checkoutPage.getCardTitles()

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            log.info(productName)
            if productName == "Blackberry":
                checkoutPage.getCardFooter(product).click()   

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        confirmPage = checkoutPage.getCheckoutItems()
        log.info("Enter country name as ind")

        self.driver.find_element(By.ID, "country").send_keys("ind")

        self.verifyLinkPresence("India")  
       
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        log.info("Text reeived from the application is"+successText)

        assert "Success! Thank you!" in successText

        self.driver.get_screenshot_as_file("screen.png")
