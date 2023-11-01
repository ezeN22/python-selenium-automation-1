from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Click on cart icon')
def search_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "image[href='https://assets.targetimg1.com/icons/assets/glyph/Cart.svg#Cart']").click()
    sleep(5)


@then('Verify your cart is empty message shown')
def verify_search(context):
    search_results_header = context.driver.find_element(By.CSS_SELECTOR, 'h1.styles__StyledHeading-sc-1xmf98v-0').text
    assert 'cart' in search_results_header, f'Expected text cart not in {search_results_header}'
    sleep(0)



@when('click on Sing in')
def search_product(context):
    context.driver.find_element(By.CSS_SELECTOR, '.styles__LinkText-sc-1e1g60c-3').click()


@when('click on Sing in button on the navigation menu')
def search_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "li#listaccountNav-signIn a span.styles__ListItemText-sc-diphzn-1").click()


@then('Verify Sign In form opened')
def verify_search(context):
    search_results_header = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert 'Sign in' in search_results_header, f'Expected text Sign in not in {search_results_header}'
    sleep(4)









