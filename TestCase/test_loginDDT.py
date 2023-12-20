import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from TestCase.Confige import setup
from PageObjectAutomation.LogPage import LoginPage
from Uilities import ExcelReadandWrite
from Uilities.customLogger import LogGen
from Uilities.readProperties import ReadConfig


class Test_LoginDDT:
    baseurl = ReadConfig.getApplicationURL()
    Excelpath = '.\\TestCase\\TestData\\Test_Data_Excel.xlsx'
    sheet = 'Sheet1'
    logger = LogGen.loggen()

    def test_case_id_003(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        row = ExcelReadandWrite.getRow(self.Excelpath, self.sheet)
        column = ExcelReadandWrite.getColumn(self.Excelpath, self.sheet)
        list_of_actual = []
        list_of_exp = []
        for i in range(2, row + 1):
            self.user = ExcelReadandWrite.getCell(self.Excelpath, self.sheet, i, 1)
            self.password = ExcelReadandWrite.getCell(self.Excelpath, self.sheet, i, 2)
            self.expResult = ExcelReadandWrite.getCell(self.Excelpath, self.sheet, i, 3)
            lp = LoginPage(self.driver)
            list_of_exp.append(self.expResult)
            if self.user == "Blank":
                self.user = ""
                self.password = ""
            lp.setUsername(self.user)
            lp.setPassword(self.password)
            lp.clickedOnLogin()
            if self.expResult == "Passed":
                result = lp.homepageValidation()
                if result:
                    self.logger.info("************test_case_id_003 data driven testing is passed***************")
                    self.logger.info("************home screen is present***************")
                    self.finalResult = "Passed"
                    lp.logout()

                else:
                    self.finalResult = "Failed"

            else:
                result = lp.error()
                self.finalResult = "Failed"

            list_of_actual.append(self.finalResult)

            if self.finalResult == self.expResult:
                self.logger.info(
                    "Combination of Username: " + self.user + " Password: " + self.password + " and expected result " + self.expResult + " is "
                                                                                                                                         " matched with actual result " + self.finalResult)

            else:
                self.logger.critical(
                    "Combination of Username: " + self.user + " Password: " + self.password + " and expected result " + self.expResult + " is not "
                                                                                                                                         " matched with actual result " + self.finalResult)

        if list_of_actual == list_of_exp:
            self.logger.info("TEST_CASE_DDT_001,TEST_CASE_DDT_002,TEST_CASE_DDT_003,TEST_CASE_DDT_004 are passed")
            assert True
        else:
            self.logger.critical("Data driven test case is failed check the logs for more details Test")
            assert False
