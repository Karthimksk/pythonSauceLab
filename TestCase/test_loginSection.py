import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from TestCase.Confige import setup
from PageObjectAutomation.LogPage import LoginPage
from Uilities.customLogger import LogGen
from Uilities.readProperties import ReadConfig


class Test_Login:
    baseurl = ReadConfig.getApplicationURL()
    UserName = ReadConfig.getUsername()
    PassWord = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_case_id_001(self,setup):
        self.logger.info("************test_case_id_001***************")
        self.driver = setup
        self.driver.get(self.baseurl)
        act = self.driver.title
        if act == "Swag Labs":
            self.logger.info("************test_case_id_001 is passed***************")
            assert True
        else:
            self.driver.save_screenshot('..\\Screenshot'+'\\testcaseTitle.png')
            self.logger.info("************test_case_id_001 is failed***************")
            assert False
    def test_case_id_002(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        lp = LoginPage(self.driver)
        lp.setUsername(self.UserName)
        lp.setPassword(self.PassWord)
        lp.clickedOnLogin()
        result = lp.homepageValidation()
        if result:
            self.logger.info("************test_case_id_002 is passed***************")
            self.logger.info("************logo is present***************")
            assert True
        else:
            self.driver.save_screenshot('..\\Screenshot'+'\\testcaseTitle.png')
            self.logger.info("************test_case_id_002 is failed***************")
            assert False

