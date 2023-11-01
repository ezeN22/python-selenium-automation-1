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
#click create your Amazon account
driver.find_element(By.ID, "createAccountSubmit").click()
# Amazon logo, search By CSS selectors class
driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')
# creat account, search by CSS selectors class
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
# your name field search by CSS Selectors attributes.
driver.find_element(By.CSS_SELECTOR, "[placeholder='First and last name']")
# mobile number or email field search by CSS selectors attributes contains with *
driver.find_element(By.CSS_SELECTOR, "[data-validation-id*='email']")
# password field search by CSS selectors ID
driver.find_element(By.CSS_SELECTOR, '#ap_password')
# password character search ny CSS selectors class
driver.find_element(By.CSS_SELECTOR, '.a-alert-content')
# Re-enter password search by CSS selectors ID
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
# continue button, search by CSS selector ID
driver.find_element(By.CSS_SELECTOR, '#continue')
# condition of use button, search by CSS Selectors attributes
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")
# privacy notice button, search by CSS Selector attributes
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")
# sing in button search by CSS Selectors attributes
driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin']")

sleep(5)
print('test pass')
driver.quit()




