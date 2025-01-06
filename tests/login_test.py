import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest
from pages.homepage import *
from pages.loginpage import *
from utils import utils
import allure
import moment




import unittest
# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))

#browswr should be open once
@pytest.mark.usefixtures("test_setup")
class TestLogin():
        # @pytest.fixture(scope="class")
        # def test_setup(self):
        #         global driver
        #         chrome_options = Options()
        #         chrome_service = Service(chrome_options=chrome_options,
        #                 executable_path=r'C:\Users\taran\PycharmProjects\AutomationFramwework1\drivers\chromedriver.exe')
        #         driver = webdriver.Chrome(service=chrome_service)
        #         driver.implicitly_wait(10)
        #         driver.maximize_window()
        #         yield
        #         driver.close()
        #         driver.quit()
        #         print("completed")

        def test_login(self):
                driver=self.driver
                # driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
                driver.get(utils.url)

                login1 = loginPage(driver)
                # login1.enter_username("Admin")
                # login1.enter_password("admin123")
                login1.enter_username(utils.username)
                login1.enter_password(utils.password)
                login1.login_btn()
                # driver.find_element(By.NAME, "username").send_keys("Admin")
                # driver.find_element(By.NAME, "password").send_keys("admin123")
                # driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
                print(driver.title)
                de = driver.title
                assert de == "OrangeHRM"
                time.sleep(3)

        def test_logout(self):
                try:

                        driver = self.driver
                        home1=homePage(driver)
                        home1.clickwelcome()
                        home1.clicklogout()
                        des = driver.title
                        assert des == "OranssgeHRM"
                except AssertionError as error:
                        currtime=moment.now().strftime("%H-%M-%S_%d_%m_%Y")
                        screenshotName="screenshot_" +currtime
                        allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,
                                      attachment_type=allure.attachment_type.PNG)
                        print("exception for assertion")
                        print(error)
                        raise

                # driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
                # driver.find_element(By.LINK_TEXT, "Logout").click()



