from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#@given('Open target main page')
#def open_target(context):
   # context.driver.get('https://www.target.com/')


@when('Search for a {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(6)  # wait for ads to disappear


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()


@when('From right side navigation menu, click Sign In')
def click_sign_in_from_nav(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@then('Verify header is present')
def verify_header_preset(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")

@then('Verify header has {number} links')
def verify_header_has_links(context, number):
    number = int(number)  # convert str to int
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    assert len(links) == number, f'Expected {number} links, but got {len(links)}'