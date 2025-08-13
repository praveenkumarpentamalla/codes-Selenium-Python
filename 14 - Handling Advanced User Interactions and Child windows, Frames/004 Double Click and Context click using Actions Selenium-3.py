from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)

action.double_click(driver.find_element(By.ID, "double-click")).perform()
alert = driver.switch_to.alert

assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()



driver.get("https://rahulshettyacademy.com/AutomationPractice/")

assert driver.find_element(By.ID, "displayed-text").is_displayed()

driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
