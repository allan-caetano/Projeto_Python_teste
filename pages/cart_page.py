from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self):
        super().__init__()
        self.basePage = BasePage()
        self.driver = conftest.driver
        self.add_cart = (By.XPATH, "//button[text()='Add to cart']")
        self.card_done = (By.XPATH, "//a[@class='shopping_cart_link']")

    def add_card(self):
        self.clicar(self.add_cart)

    def show_cart(self):
        self.clicar(self.card_done)
