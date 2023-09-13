import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver: webdriver.Remote


@pytest.fixture
def setup():
    global driver
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')

    # run teste
    yield

    driver.quit()
