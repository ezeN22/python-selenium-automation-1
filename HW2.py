from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get("https://www.amazon.com/")
sleep(6)

#Click Signin Nav button
driver.find_element(By.ID, "nav-link-accountList").click()

# Amazon logo, search By Xpath, tag and attribute.
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Email field, search by ID
driver.find_element(By.ID, "ap_email")

# Continue button, search by ID
driver.find_element(By.ID, "continue")
# continue button, search by XPATH
driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']")

# Conditions of use link Search by XPATH, text
driver.find_element(By.XPATH, "//a[text()= 'Conditions of Use']")

# Privacy Notice link, search by XPATH, text
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

# Need help link search by XPATH
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot your password link, search by ID
driver.find_element(By.ID, "auth-fpp-link-bottom")

# Other issues with Sign-In link, search by
driver.find_element(By.ID, "ap-other-signin-issues-link")

# Create your Amazon account button, search by
driver.find_element(By.ID, "createAccountSubmit")

sleep(5)
print('Test Passed')
driver.quit()

