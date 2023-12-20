from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

from PageObjectAutomation.LogPage import LoginPage


class ProductPage:
    All_img_XPATH = '// img[ @class ="inventory_item_img"]'
    All_productheadlines_XPATH = '// div[@ class ="inventory_item_name"]'
    ALL_price_XPATH = '// div[@ class ="inventory_item_price"]'
    Filter_Icon_XPATH = '//select[@class = "product_sort_container"]'
    Product_Line_XPATH = "//div[normalize-space()='Sauce Labs Backpack']"
    InsideProduct_Line_XPATH = "//div[@class='inventory_details_name large_size']"
    InsideProduct_Price_XPATH = "//div[@class='inventory_details_price']"
    InsideProduct_Img_XPATH= "//img[@alt='Sauce Labs Backpack']"
    def __init__(self, driver):
        self.driver = driver
    @property
    def getAllImage(self):
        list_img = self.driver.find_elements(By.XPATH, self.All_img_XPATH)
        num = len(list_img)
        list_imgresult = []
        for i in range(0, num):
            list_imgresult.append(list_img[i].is_displayed())
        if all(list_imgresult):
            return num,True
        else:
            return False

    @property
    def getAllProduct(self):
        list_pro = self.driver.find_elements(By.XPATH, self.All_productheadlines_XPATH)
        num = len(list_pro)
        list_proAc = []
        for i in range(0, num):
            list_proAc.append(list_pro[i].text)
        return num, list_proAc

    @property
    def getAllPrice(self):

        list_price = self.driver.find_elements(By.XPATH, self.ALL_price_XPATH)
        num = len(list_price)
        list_priAc = []
        for i in range(0, num):
            list_priAc.append(float(list_price[i].text.replace('$', '')))
        return num, list_priAc

    def clickedFilterIcon(self):
        self.driver.find_element(By.XPATH, self.Filter_Icon_XPATH).click()
    def AtoZFilter(self):
        option = Select(self.driver.find_element(By.XPATH,self.Filter_Icon_XPATH))
        option.select_by_value("az")
    def ZtoAFilter(self):
        option = Select(self.driver.find_element(By.XPATH, self.Filter_Icon_XPATH))
        option.select_by_value("za")
    def LtoHFilter(self):
        option = Select(self.driver.find_element(By.XPATH, self.Filter_Icon_XPATH))
        option.select_by_value("lohi")
    def HtoLFilter(self):
        option = Select(self.driver.find_element(By.XPATH, self.Filter_Icon_XPATH))
        option.select_by_value("hilo")

    def OneProduct(self):
        self.driver.find_element(By.XPATH, self.Product_Line_XPATH).click()
        ResultHeadLines = self.driver.find_element(By.XPATH, self.InsideProduct_Line_XPATH).is_displayed()
        ResultPrice = self.driver.find_element(By.XPATH, self.InsideProduct_Price_XPATH).is_displayed()
        ResultImg = self.driver.find_element(By.XPATH, self.InsideProduct_Img_XPATH).is_displayed()
        if ResultImg == ResultPrice == ResultHeadLines == True:
            return True
        else:
            return False
