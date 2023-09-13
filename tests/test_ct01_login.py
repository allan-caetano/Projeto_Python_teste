import pytest
import allure
import conftest
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures('setup')
@pytest.mark.login
@allure.feature('Login')
class TesteCT01:
    def test_ct01_login(self):
        driver = conftest.driver
        basePage = BasePage()
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()

        basePage.espera_sleep(1)
        login_page.fazer_login('standard_user', 'secret_sauce')
        home_page.verificar_title()

        basePage.espera_sleep(3)
        cart_page.add_card()
        cart_page.show_cart()
        login_page.verificar_texto_existe('Sauce Labs Backpack')
