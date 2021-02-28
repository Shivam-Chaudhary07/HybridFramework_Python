from selenium import webdriver
import pytest

#onsist of all the common details for all TCs

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox
    else:
        driver = webdriver.Chrome()  #this is default browser
    return driver

def pytest_addoption(parser): #this will get values from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #this will return browser value to setup method
    return request.config.getoption("--browser")

### Pytest HTML Reports ###

#this hook add env info to html report
"""def pytest_configure(config):
    config.metadata['Project Name'] =   'nop commerce'
    config.metadata['Module Name'] = 'Customers'
    config.metadata['Tester'] = 'Shivam'

#this hook is to delete/modify environment info in html reports
@pytest.mark.optionalhook
def pystest_metadata(metadata):
    metadata.pop('Java_Home', None)
    metadata.pop("Plugins", None)"""