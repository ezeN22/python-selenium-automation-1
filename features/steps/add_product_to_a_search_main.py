from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#@then('Verify search worked for {product}')
#def verify_search(context, product):
    #search_results_header = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
    #assert product in search_results_header, f'Expected text {product} not in {search_results_header}'


@when('click on the product')
def search_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='/p/basic-reusable-tote-bag-red']").click()
    sleep(3)



@when('store product name')
def get_product_name(context):
    context.product_name = context.driver.find_element(By.CSS_SELECTOR, '#pdp-product-title-id').text
    print(f'correct context: {context.product_name}')


@when('click on add to cart button')
def add_to_cart_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label='Add to cart for Basic Reusable Tote Bag Red']") .click()


@when('open cart page')
def open_cart_page(context):
    context.driver.find_element(By.CSS_SELECTOR,'.h-text-lg')


@then('verify cart has 1 item(s)')
def cat_has_1_item(context):
    context.driver.find_element(By.CSS_SELECTOR,'.styles__CartQuantity-sc-jff2tp-1')




@then('verify cart has correct product')
def cart_has_correct_product(context):
    search_results_header = context.driver.find_element(By.CSS_SELECTOR,'#pdp-product-title-id').text
    expected_text = 'Tote Bag'
    assert expected_text in search_results_header, f'Expected text {expected_text} not in {search_results_header}'






