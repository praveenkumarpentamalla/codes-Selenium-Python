from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Automatically downloads compatible driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://login.salesforce.com/?locale=in")

driver.find_element(By.ID, "username").send_keys("PraveenKaumar")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("kumar")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#password").clear()
driver.find_element(By.LINK_TEXT, "Forgot Your Password?").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@value='Cancel']").click()

print(driver.find_element(By.XPATH, "//form[@name='login']/div[1]/label").text)

# print(driver.find_element(By.CSS_SELECTOR, "form[name='login'] label:nth-child(3)").text)
print(driver.find_element(By.CSS_SELECTOR, "form[name='login'] label[for='password']").text)


print("Title:", driver.title)
print("URL:", driver.current_url)

time.sleep(2)

