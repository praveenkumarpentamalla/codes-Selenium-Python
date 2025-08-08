from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

# Automatically download and setup the ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the website
driver.get("https://management.divsolution.com/")
driver.maximize_window()

# Print title and URL
print("Title:", driver.title)
print("URL:", driver.current_url)

# Locate the email input using the correct name or ID
# From your HTML: name="email_temp", id="id_email"
driver.find_element(By.NAME, "email_temp").send_keys("praveenkumar")

# Alternatively, using ID:
# driver.find_element(By.ID, "id_email").send_keys("praveenkumar")






## Using CSS Selectors ##


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Automatically downloads compatible driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://sso.teachable.com/secure/9521/identity/sign_up/otp")
driver.maximize_window()

print("Title:", driver.title)
print("URL:", driver.current_url)


driver.find_element(By.CSS_SELECTOR, "#name").send_keys("praveenkumar")
driver.find_element(By.CSS_SELECTOR, "#allowMarketingEmails").click()

driver.maximize_window()
driver.minimize_window()







# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# # Automatically downloads compatible driver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get("https://www.rahulshettyacademy.com/practice")  

# # Fill the form  
# driver.find_element_by_name("name").send_keys("Rahul")  
# driver.find_element_by_name("email").send_keys("test@example.com")  
# driver.find_element_by_id("password").send_keys("123456")  

# # Select checkbox  
# driver.find_element_by_id("agreeTerms").click()  

# # Submit form  
# driver.find_element_by_css_selector("#submitBtn").click()  

# driver.quit()  
