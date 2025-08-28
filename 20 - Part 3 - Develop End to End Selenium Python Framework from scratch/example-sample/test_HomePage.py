from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from BaseClass import BaseClass
from HomePage import HomePage
import pytest
from HomePageData import HomePageData

class TestHomePage(BaseClass):

    def test_formSubmissions(self, getData):
        log = self.getlogger()
        log.info("First name is"+getData[0])

        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData[0])
        homepage.getEmail().send_keys(getData[1])
        homepage.getCheck().click()
        self.selectOptionByText(homepage.getGender(), getData[2])
        homepage.submitForm().click()

        alertText = homepage.successMessage().tetxt

        assert "Success!" in alertText
        self.driver.refresh()


# @pytest.fixture(params=[("praveen", "kumar", "Male"), ("Kumar", "Praveen", "Male")])

@pytest.fixture(params=HomePageData.test_HomePage_data)
def getData(self, request):
    return request.param
