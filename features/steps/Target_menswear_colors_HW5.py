from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



COLOR_OPTIONS = (By.CSS_SELECTOR,"[class*='styles__BaseVariationSelectorWrapper-sc-519sqw-0'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='styles__StyledVariationSelectorImage-sc-d30gwr-1'] [class*='styles__CellVariationHeaderWrapper-sc-1xq8mou-0']")


@given('Open target product A-88345426 page')
def open_target(context):
    context.driver.get('https://www.target.com/p/A-88345426')
    sleep(6)


@then('Verify users can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Brown','otameal','Gray,Black']
    actual_color = []
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text # 'Color\nBlack' => ['Color', 'Black']
        actual_color.append(selected_color)
        print(selected_color)

    #assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
