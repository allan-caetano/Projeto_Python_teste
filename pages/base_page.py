import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
import time


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)

    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)

    def digitar(self, locator, text):
        self.encontrar_elemento(locator).send_keys(text)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

    def existe_elemento(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), f'O elemento não {locator} foi encontado'

    def pegar_texto(self, locator):
        #  self.espera_elemento(locator)
        return self.encontrar_elemento(locator).text

    def espera_elemento(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator))

    def espera_sleep(self, timeout):
        return time.sleep(timeout)

    def verifia_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator), f'O Elemento {locator}  não existe'

    def dou_click(self, locator):
        elemento = self.encontrar_elemento(locator)
        ActionChains(self.driver).double_click(elemento).perform()

    def clicar_direito(self, locator):
        elemento = self.encontrar_elemento(locator)
        ActionChains(self.driver).context_click(elemento).perform()

    def teclar(self, locator, key):
        elemento = self.encontrar_elemento(locator)
        if key == 'ENTER':
            elemento.send_keys(Keys.ENTER)
        elif key == 'TAB':
            elemento.send_keys(Keys.TAB)
        elif key == 'SPACE':
            elemento.send_keys(Keys.SPACE)
        else:
            print('Não foi fornecido uma Teca Valida')
