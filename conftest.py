import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="session")
def browser():
    # driver = webdriver.Chrome(executable_path="./chromedriver")
    # driver = webdriver.Firefox(executable_path=r'./geckodriver')

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path=r'./geckodriver')
    yield driver
    driver.quit()



