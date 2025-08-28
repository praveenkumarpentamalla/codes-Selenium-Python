import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from CheckoutPage import CheckoutPage 



class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop]")
    name = (By.CSS_SELECTOR, "[name='name]")
    email = (By.CSS_SELECTOR, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "examplwFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")




    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver) 
        return checkoutPage
    
    def getName(self):
        return self.driver.find_element(*HomePage.name)
    
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
    
    def getCheck(self):
        return self.driver.find_element(*HomePage.check)
    def getGender(self):
            return self.driver.find_element(*HomePage.gender)
    def getSubmit(self):
            return self.driver.find_element(*HomePage.submit)
    def getMessage(self):
            return self.driver.find_element(*HomePage.successMessage)
