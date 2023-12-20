from PageObjectAutomation.ProducToCartPage import CartPage
from Uilities.customLogger import LogGen
from Uilities.readProperties import ReadConfig
from PageObjectAutomation.LogPage import LoginPage
from TestCase.Confige import setup


class TestCart:
    baseurl = ReadConfig.getApplicationURL()
    UserName = ReadConfig.getUsername()
    PassWord = ReadConfig.getPassword()
    logger = LogGen.loggen()
    def test_case_ID_12(self, setup):
        self.driver = setup
        # login page Objext
        lp = LoginPage(self.driver)
        self.driver.get(self.baseurl)
        lp.setUsername(self.UserName)
        lp.setPassword(self.PassWord)
        lp.clickedOnLogin()
        self.pc = CartPage(self.driver)
        ActualResult1 = self.pc.selectProduct()
        ActualResult2 = self.pc.checkingOnCart()
        if ActualResult2 == ActualResult1 == True:
            assert True
        else:
            assert False
