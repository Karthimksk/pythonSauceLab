import selenium
from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    # Setup code
    driver = webdriver.Chrome(".\\Drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Provide the WebDriver instance to the test
    yield driver

    # Teardown code (runs after the test)
    driver.quit()

def pytest_configure(config):
    config.stash[metadata_key]["Application Name"] = "Sauce Lab"
    config.stash[metadata_key]["Tester Name"] = "Karthikeyan M"
