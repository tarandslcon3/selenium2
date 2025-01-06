from selenium.webdriver.common.by import By


class homePage():
    def __init__(self,driver):
        self.driver = driver
        self.welcome_xpath = "//span[@class='oxd-userdropdown-tab']"
        self.logout_link = "Logout"

    def clickwelcome(self):
        self.driver.find_element(By.XPATH,self.welcome_xpath).click()
    def clicklogout(self):
        self.driver.find_element(By.LINK_TEXT,self.logout_link).click()