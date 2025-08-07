from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Automatically downloads compatible driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.rahulshettyacademy.com/practice")  

# Fill the form  
driver.find_element_by_name("name").send_keys("Rahul")  
driver.find_element_by_name("email").send_keys("test@example.com")  
driver.find_element_by_id("password").send_keys("123456")  

# Select checkbox  
driver.find_element_by_id("agreeTerms").click()  

# Submit form  
driver.find_element_by_css_selector("#submitBtn").click()  

driver.quit()  
