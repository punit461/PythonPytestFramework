from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        service = Service(
            executable_path='C:\drivers\chromedriver.exe')  # selenium 4.10 webdriver.chrome accepts service & options
        options = webdriver.ChromeOptions()  # add capabilities
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        # driver = webdriver.Chrome()
        print("Launching Chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser.........")
    else:
        driver = webdriver.Ie()
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


#############  PyTest HTML Report #####################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    # config._metadata['Project Name'] = 'nop Commerce'
    # config._metadata['Module Name'] = 'Customers'
    # config._metadata['Tester'] = 'Pavan'
    config._metadata = {
        "Tester": "Punit",
        "Module Name": "Customers",
        "Project Name": "nop Commerce Hybrid Framework Practice",
    }


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
