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
        homePage = HomePage(self.driver)
        homePage.shopItems().click()

        checkoutPage = CheckoutPage(self.driver)   

        products = checkoutPage.getCardTitles()

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                checkoutPage.getCardFooter(product).click()   

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        checkoutPage.getCheckoutItems().click()

        self.driver.find_element(By.ID, "country").send_keys("ind")

        wait = WebDriverWait(self.driver, 7)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))

        self.driver.find_element(By.PARTIAL_LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success! Thank you!" in successText

        self.driver.get_screenshot_as_file("screen.png")

