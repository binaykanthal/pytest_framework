from selenium.webdriver.common.by import By

from pages.login_page import LoginPage

def test_login_page(browser):
    browser.get("https://rahulshettyacademy.com/client")
    login_page = LoginPage(browser)
    cart_page = login_page.login("binaykanthal@gmail.com", "passWord1*")
    assert cart_page.search_confirmation() == "Search"
