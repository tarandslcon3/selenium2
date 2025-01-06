from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chromeservice
from selenium.webdriver.chrome.options import Options as Chromeoptions
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as firefoxservice
from selenium.webdriver.firefox.options import Options as firefoxoptions
import pytest



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g.chrome OR firefox")

@pytest.fixture(scope="class")
def test_setup(request):
    # global driver
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        chrome_options = Chromeoptions()
        chrome_service = Chromeservice(chrome_options=chrome_options,
            executable_path=r'C:\Users\taran\PycharmProjects\AutomationFramwework1\drivers\chromedriver.exe')
        driver = webdriver.Chrome(service=chrome_service)
    elif browser == 'firefox':
        firefox_options = firefoxoptions()
        firefox_service = firefoxservice(firefox_options=firefox_options,
                                 executable_path=r'C:\Users\taran\PycharmProjects\AutomationFramwework1\drivers\geckodriver.exe')
        driver = webdriver.Firefox(service=firefox_service)

    request.cls.driver=driver
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("completed")