from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Automatically downloads compatible driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.rahulshettyacademy.com")

print("Title:", driver.title)
print("URL:", driver.current_url)

driver.quit()




# from selenium import webdriver  

# # Initialize Chrome  
# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")  

# # Open a website  
# driver.get("https://www.rahulshettyacademy.com")  

# # Print title and URL  
# print("Title:", driver.title)  
# print("URL:", driver.current_url)  

# # Close the browser  
# driver.quit()  
