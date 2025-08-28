from selenium.webdriver.common.by import By
from ConfirmPage import ConfirmPage

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitles = (By.XPATH, "//div[@class='card h-100']")
    cardFooter = (By.XPATH, "div/button")
    checkout = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitles)

    def getCardFooter(self, product):
        return product.find_element(*CheckoutPage.cardFooter)

    def getCheckoutItems(self):
        self.driver.find_element(*CheckoutPage.checkout).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
