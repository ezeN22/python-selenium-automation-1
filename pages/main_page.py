from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class MainPage(Page):
    #SEARCH_FIELD = (By.ID, 'search')
    #SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "image[href='https://assets.targetimg1.com/icons/assets/glyph/Cart.svg#Cart']")
    SIGN_IN = (By.CSS_SELECTOR, '.styles__LinkText-sc-1e1g60c-3')
    SIDE_SIGN_IN_BTN = ("li#listaccountNav-signIn a span.styles__ListItemText-sc-diphzn-1")

    def open_main(self):
        self.open_url('https://www.target.com/')

    #def search(self, product):
        #self.input(product, *self.SEARCH_FIELD)
        #self.click(*self.SEARCH_BTN)
        sleep(6)  #wait for ads to disappear

    def click_cart(self):
         self.click(*self.CART_ICON)

    def click_on_sign_in(self):
         self.click('click on sign in', *self.SIGN_IN)


    def click_on_Sing_in_button_on_the_navigation_menu(self):
         self.click('click on sign in button on the navigation menu', *self.SIDE_SIGN_IN_BTN)










