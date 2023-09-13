import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        self.driver = conftest.driver
        self.title_page = (By.XPATH, "//span[@class='title']")

    def verificar_title(self):
        self.existe_elemento(self.title_page)

