from selenium.webdriver.common.by import By

from pages.CartPage import CartPage
from pages.base_page import BasePage


class LoginPage(BasePage):
    user_name = (By.ID, "userEmail")
    pass_word = (By.ID, "userPassword")
    submit_btn = (By.ID, "login")

    def login(self, username, password):
        self.send_keys(self.user_name, username)
        self.send_keys(self.pass_word, password)
        self.click(self.submit_btn)
        return CartPage(self.driver)