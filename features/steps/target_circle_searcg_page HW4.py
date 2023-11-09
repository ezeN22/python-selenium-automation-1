from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#@given('Open target main page')
#def open_target(context):
  #  context.driver.get('https://www.target.com/')



@then('Verify header has {number} benefit')
def verify_header_has_links(context, number):
        number = int(number)  # convert str to int
        benefit = context.driver.find_elements(By.CSS_SELECTOR,"[class*='styles__BenefitsGrid-sc-9mx6dj-1'] li")
        assert len(benefit) == number, f'Expected {number} benefit, but got {len(benefit)}'
