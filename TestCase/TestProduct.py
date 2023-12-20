import os

from TestCase.Confige import setup
from PageObjectAutomation.LogPage import LoginPage
from PageObjectAutomation.ProductBrowseringPage import ProductPage
from Uilities import ExcelReadandWrite
from Uilities.customLogger import LogGen
from Uilities.readProperties import ReadConfig

class TestFilter:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    Excelpath = os.getcwd() + '\\TestCase\\TestData\\Test_Data_Excel.xlsx'
    sheet = 'Sheet1'
    logger = LogGen.loggen()
    def test_case_ID_006(self, setup):
        self.driver=setup
        #login page Objext
        lp = LoginPage(self.driver)
        self.driver.get(self.baseurl)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickedOnLogin()
        #validation for img checking
        pb = ProductPage(self.driver)
        ActualImg = pb.getAllImage
        #validation for price
        ActualPrice = pb.getAllPrice
        #validation for product Headlines
        ActualProduct = pb.getAllProduct
        if ActualImg[1] == True and ActualPrice[0]==ActualProduct[0]==ActualImg[0]:
            self.logger.info("Test Case ID 006 Passed all image, price and headlines are displayed")
            assert True
        else:
            self.logger.info("Test Case ID 006 is failed")
            assert False
    def test_case_ID_007 (self, setup):
        self.driver = setup
        # login page Objext
        lp = LoginPage(self.driver)
        self.driver.get(self.baseurl)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickedOnLogin()
        # validation for one product img, headline and price
        pb = ProductPage(self.driver)
        ActualResult = pb.OneProduct()
        if ActualResult:
            self.logger.info("Test Case ID 007 is passed")
            assert True
        else:
            self.logger.info("Test Case ID 007 is faiiled")

    def test_case_ID_008(self, setup):
        self.driver = setup
        # login page Objext
        lp = LoginPage(self.driver)
        self.driver.get(self.baseurl)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickedOnLogin()
        # validation for A to Z
        pb = ProductPage(self.driver)
        pb.clickedFilterIcon()
        pb.AtoZFilter()
        ActualList = pb.getAllProduct
        ExcelRead = ExcelReadandWrite
        List = []
        for i in range(2, ActualList[0]+2):
            Temp = ExcelRead.getCell(os.getcwd()+"\\TestData\\Test_Data_Excel.xlsx",'Sheet2',i, c=2)
            List.append(Temp)
        ExpectedList = sorted(List)
        if ActualList[1]==ExpectedList:
            self.logger.info("Test Case ID 008 is passed")
            assert True
        else:
            self.logger.info("Test caes ID 008 is failed")
            print(ActualList)
            print(ExpectedList)
            assert False

    def test_case_ID_009(self, setup):
        self.driver = setup
        # login page Objext
        lp = LoginPage(self.driver)
        self.driver.get(self.baseurl)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickedOnLogin()
        # validation for Z to A
        pb = ProductPage(self.driver)
        pb.clickedFilterIcon()
        pb.ZtoAFilter()
        ActualList = pb.getAllProduct
        ExcelRead = ExcelReadandWrite
        List = []
        for i in range(2, ActualList[0]+2):
            Temp = ExcelRead.getCell(os.getcwd()+"\\TestData\\Test_Data_Excel.xlsx",'Sheet2',i, c=2)
            List.append(Temp)
        ExpectedList = sorted(List)
        ExpectedList.reverse()
        if ActualList[1]== ExpectedList:
            self.logger.info("Test Case ID 009 is passed")
            assert True
        else:
            self.logger.info("Test caes ID 009 is failed")
            print(ActualList)
            print(ExpectedList)
            assert False

    def test_case_ID_010(self, setup):
        self.driver = setup
        # login page Objext
        lp = LoginPage(self.driver)
        self.driver.get(self.baseurl)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickedOnLogin()
        # validation for L to H
        pb = ProductPage(self.driver)
        pb.clickedFilterIcon()
        pb.LtoHFilter()
        ActualList = pb.getAllPrice
        ExcelRead = ExcelReadandWrite
        List = []
        for i in range(2, ActualList[0]+2):
            Temp = ExcelRead.getCell(os.getcwd()+"\\TestData\\Test_Data_Excel.xlsx",'Sheet2',i, c=1)
            List.append(Temp)
        ExpectedList = sorted(List)
        if ActualList[1]== ExpectedList:
            self.logger.info("Test Case ID 010 is passed")
            assert True
        else:
            self.logger.info("Test caes ID 010 is failed")
            print(ActualList)
            print(ExpectedList)
            assert False

    def test_case_ID_011(self, setup):
        self.driver = setup
        # login page Objext
        lp = LoginPage(self.driver)
        self.driver.get(self.baseurl)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickedOnLogin()
        # validation for H to L
        pb = ProductPage(self.driver)
        pb.clickedFilterIcon()
        pb.HtoLFilter()
        ActualList = pb.getAllPrice
        ExcelRead = ExcelReadandWrite
        List = []
        for i in range(2, ActualList[0]+2):
            Temp = ExcelRead.getCell(os.getcwd()+"\\TestData\\Test_Data_Excel.xlsx",'Sheet2',i, c=1)
            List.append(Temp)
        ExpectedList = sorted(List)
        ExpectedList.reverse()
        if ActualList[1]== ExpectedList:
            self.logger.info("Test Case ID 011 is passed")
            assert True
        else:
            self.logger.info("Test caes ID 011 is failed")
            print(ActualList)
            print(ExpectedList)
            assert False