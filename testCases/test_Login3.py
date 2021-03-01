from utilities.customLogger import LogGen
from selenium import webdriver
from utilities.readProperties import ReadConfig
import pytest


class Test_Log:

    baseURL = ReadConfig.getAppURL()  # using readProperties from utilities
    username = 'admin@yourstore.com'
    password = 'admin'

    log = LogGen.loggen()
    log.info("Start Logs")

    @pytest.mark.sanity
    def test_logStart(self):

        self.driver = webdriver.Chrome()
        self.log.info("Driver start")
        self.driver.get(self.baseURL)
        self.log.info("URL launched")
        self.log.info("closing driver")
        self.driver.close()

if __name__ == "__main__":
    t = Test_Log()
    t.test_logStart()