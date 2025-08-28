import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
import inspect
import logging

@pytest.mark.usefixtures("setup")

class BaseClass:
    
    def getlogger(self):
         loggerName = inspect.stack()[1][3]
         logger = logging.getLogger(loggerName)
         fileHandler = logging.FileHandler('logfile.log')
         formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
         fileHandler.setFormatter(formatter)

         logger.addHandler(fileHandler)

         logger.setLevel(logging.DEBUG)
         return logger
    
    def verifyLinkPresence(self, text):
         wait = WebDriverWait(self.driver, 7)
         wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
         sel = Select(locator)
         sel.select_by_visible_text("Male")
