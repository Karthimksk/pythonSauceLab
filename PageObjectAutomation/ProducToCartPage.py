import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from Uilities.readProperties import ReadConfig
class CartPage:

    def __init__(self, driver):
        self.driver = driver

    objectConfig = ReadConfig
    NameOfProductFromConfig = objectConfig.getProductName()
    Product_Headlines_LINKTEXT = NameOfProductFromConfig
    Card_icon_ID = "shopping_cart_link"
    Cart_num_XPATH = "//span[contains(text(),'1')]"
    AddCart_button_ID = "add-to-cart-" + NameOfProductFromConfig.replace(" ", "-").lower()
    Price_Text_XPATH = '//div[@class="inventory_item_price"]'


    def selectProduct(self):
        self.driver.find_element(By.LINK_TEXT, self.Product_Headlines_LINKTEXT)
        self.driver.find_element(By.ID, self.AddCart_button_ID).click()
        time.sleep(3)
        num = self.driver.find_element(By.ID, self.Cart_num_XPATH).is_displayed()
        if num:
            return True
        else:
            return False


    def checkingOnCart(self):
        self.driver.find_element(By.ID, self.Card_icon_ID).click()
        resultOfText = self.driver.find_element(By.LINK_TEXT, self.Product_Headlines_LINKTEXT).is_displayed()
        resyltOfPrice = self.driver.find_element(By.XPATH, self.Price_Text_XPATH).is_displayed()
        if (resyltOfPrice == resyltOfPrice == True):
            return True
        else:
            return False