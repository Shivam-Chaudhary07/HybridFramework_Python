import pytest
from pageObjects.LoginPage import Login
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:

    #baseURL = 'https://admin-demo.nopcommerce.com/'
    baseURL = ReadConfig.getAppURL() #using readProperties from utilities
    username = 'admin@yourstore.com'
    password = 'admin'

    log = LogGen.loggen()
    log.info('Start logs')

    @pytest.mark.regression
    def test_01_HomePageTitle(self):


        self.log.info("**** logs verified HomePage Title started ***")
        self.driver = webdriver.Chrome()
        print(self.baseURL)
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
                assert True
                self.log.info("**** logs verified HomePage Title matched ***")
                self.driver.close()

        else:
                self.log.error("**** logs verified HomePage Title mismatched ***")
                self.driver.save_screenshot("..\\Screenshots\\HomePageTitle.png")
                self.driver.close()
                assert False



    def test_02_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLogin()
        chk_login = self.driver.title
        if chk_login == "Dashboard / nopCommerce administration":
            
                assert True
                self.driver.close()

        else:
                self.driver.save_screenshot("..\\Screenshots\\test_02_login.png")
                self.driver.close()
                assert False

    """def test_03_login(self, setup): #using pytest fixture >> setup
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLogin()

if __name__ == '__main__':
    t = Test_001_Login()
    t.test_01_HomePageTitle()"""