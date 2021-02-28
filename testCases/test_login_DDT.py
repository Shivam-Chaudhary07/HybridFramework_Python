from pageObjects.LoginPage import Login
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest
from utilities import ExcelUtil
import time


class Test_DDT_Login:
    baseURL = ReadConfig.getAppURL()  # using readProperties from utilities
    path = "..//TestData/Test_login.xlsx"

    log = LogGen.loggen()
    log.info('Start logs')

    def test_02_DDT_login(self, setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)

        self.rows = ExcelUtil.getRowCount(self.path, "Sheet1")
        print("total rows", self.rows)

        lst_status = []

        for r in range(2, self.rows+1):

            self.username = ExcelUtil.readData(self.path, "Sheet1", r, 1)
            self.password = ExcelUtil.readData(self.path, "Sheet1", r, 2)
            self.exp = ExcelUtil.readData(self.path, "Sheet1", r, 3)

            self.lp.enterUsername(self.username)
            self.lp.enterPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            chk_login = self.driver.title
            if chk_login == "Dashboard / nopCommerce administration":
                if self.exp=='Pass':
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp =='Fail':
                    self.lp.clickLogout()
                    lst_status.append("Failed")


                if chk_login != "Dashboard / nopCommerce administration":

                    if self.exp == 'Pass':

                        lst_status.append("Failed")
                    elif self.exp == 'Fail':

                        lst_status.append("Pass")

        if "Fail" not in lst_status:
            print("Test Success")
            ExcelUtil.writeData(self.path, "Sheet1", 6, 4, "Accepted")
            self.driver.close()

        else:
            print("Test Failed")
            ExcelUtil.writeData(self.path, "Sheet1", 6, 4, "Failed")
            self.driver.close()


if __name__ == '__main__':
    DDT = Test_DDT_Login()
    DDT.test_02_DDT_login()




