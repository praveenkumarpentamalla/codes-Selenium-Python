from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
import time

list = []
list2 = []

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))



driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")


driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")

time.sleep(4)

count = len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))
assert count == 3

buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")


for button in buttons:
    list.append(button.find_element(By.XPATH, "parent::div/parent::div/h4").text)
    button.click()

print(list)


driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))


veggies = driver.find_elements(By.CSS_SELECTOR, "p.product-name")

for veg in veggies:
    list2.append(veg.text)

print(list2)


assert list == list2

original_amount = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))

discount_amount = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)


assert float(discount_amount) < int(original_amount)

amounts = driver.find_elements(By.XPATH, "//tr/td[5]/p")

summ = 0

for amount in amounts:
    summ = summ + int(amount.text)

print(summ)

totalAmt = int(driver.find_element(By.CLASS_NAME, "totAmt").text)

assert summ == totalAmt
