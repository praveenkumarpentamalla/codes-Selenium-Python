from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


validatetext = "option1"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID, "name").send_keys(validatetext)

driver.find_element(By.ID, "alertbtn").click()

alret = driver.switch_to.alert
# print(alret.text)
alrettext = alret.text
assert validatetext in alrettext
time.sleep(2)
alret.accept()

driver.find_element(By.ID, "name").send_keys(validatetext)
driver.find_element(By.ID, "confirmbtn").click()
confirm_alert  = driver.switch_to.alert
# print(alret.text)
confirm_text  = confirm_alert.text
print(confirm_text)
assert validatetext in confirm_text
time.sleep(2)
alret.dismiss()

