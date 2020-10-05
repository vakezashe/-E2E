import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    # driver = webdriver.Chrome(executable_path="./chromedriver")
    driver = webdriver.Firefox(executable_path=r'./geckodriver')
    yield driver
    # driver.quit()