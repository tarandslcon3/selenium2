from selenium.webdriver.common.by import By

class loginPage():
    def __init__ (self,driver):
        self.driver = driver
        self.username_by_name = "username"
        self.password_by_name = "password"
        self.loginbtn_xpath = "//button[normalize-space()='Login']"

    def enter_username(self,username):
        self.driver.find_element(By.NAME, self.username_by_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME,self.password_by_name).send_keys(password)

    def login_btn(self):
        self.driver.find_element(By.XPATH,self.loginbtn_xpath).click()


