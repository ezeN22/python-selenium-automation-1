from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    HEADER = (By.CSS_SELECTOR, 'h1.styles__StyledHeading-sc-1xmf98v-0')

    def verify_cart_empty_txt(self):
        expected = 'Your cart is empty'
        actual = self.find_element(*self.HEADER).text
        assert expected == actual, f'Expected {expected} did not match actual {actual}'