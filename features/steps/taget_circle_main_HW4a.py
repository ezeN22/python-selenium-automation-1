from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Click target circle')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR,'#utilityNav-circle').click()




