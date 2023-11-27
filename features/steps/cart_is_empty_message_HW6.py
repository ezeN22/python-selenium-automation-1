from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def search_product(context):
    context.app.main_page.open_main()


@when('Click on cart icon')
def click_cart(context):
    context.app.main_page.click_cart()



@then('Verify cart is empty message shown')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty_txt()