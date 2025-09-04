from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, "section b")

    def search_confirmation(self):
        return self.get_text(self.CART_ITEMS)
