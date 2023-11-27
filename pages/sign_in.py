from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):

    SIGN_IN_FORM = (By.XPATH, "//span[text()='Sign into your Target account']")

    def verify_sign_in_form_opened(self):
        self.verify_text('sign in form opened', *self.SIGN_IN_FORM)







