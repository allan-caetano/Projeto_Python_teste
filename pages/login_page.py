import conftest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.basePage = BasePage()
        self.driver = conftest.driver
        self.username_field = (By.ID, 'user-name')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')
        self.texto_produto = (By.XPATH, "//div[text()='Sauce Labs Backpack']")

    def fazer_login(self, usuario, senha):
        self.digitar(self.username_field, usuario)
        self.digitar(self.password_field, senha)
        # self.basePage.teclar(self.login_button, 'ENTER')
        self.clicar(self.login_button)

    def verificar_texto_existe(self, texto_esperado):
        assert self.pegar_texto(self.texto_produto) == texto_esperado, f" O texto retornado foi outro"
