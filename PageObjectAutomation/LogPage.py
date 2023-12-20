from selenium import webdriver
from selenium.webdriver.common.by import By
from TestCase.Confige import setup


class LoginPage:
    text_user_name_ID = "user-name"
    text_password_ID = "password"
    button_login_ID = "login-button"
    message_error_XPATH = "//h3[@data-test='error']"
    homeScreen_swag_XPATH = "//div[@id='inventory_container']//div//div[@id='inventory_container']"
    button_menu_ID = "react-burger-menu-btn"
    button_logout_ID = "logout_sidebar_link"
    def __init__(self, driver):
        self.driver = driver
    def getBase(self, baseURL):
        self.driver.get(baseURL)
    def setUsername(self, username):
        self.driver.find_element(By.ID, self.text_user_name_ID).clear()
        self.driver.find_element(By.ID, self.text_user_name_ID).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.text_password_ID).clear()
        self.driver.find_element(By.ID, self.text_password_ID).send_keys(password)

    def clickedOnLogin(self):
        self.driver.find_element(By.ID, self.button_login_ID).click()
    def homepageValidation(self):
        try:
            result = self.driver.find_element(By.XPATH, self.homeScreen_swag_XPATH).is_displayed()
            return result
        except:
            return False
    def logout(self):
        self.driver.find_element(By.ID, self.button_menu_ID).click()
        self.driver.find_element(By.ID, self.button_logout_ID).click()

    def error(self):
        errorResult = self.driver.find_element(By.XPATH, self.message_error_XPATH).is_displayed()
        return errorResult
