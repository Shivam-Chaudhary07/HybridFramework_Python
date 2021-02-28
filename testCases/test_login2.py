from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.customLogger import LogGen

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://admin-demo.nopcommerce.com/')

log = LogGen.loggen()
print(log)
log.info("test started")

lgn = Login(driver)
lgn.enterUsername('admin@yourstore.com')
lgn.enterPassword('admin')
lgn.clickLogin()
driver.save_screenshot("C:\\Users\\dell\\Pictures\\Screenshots\\ss.png")
act = lgn.driver.title  #imp to use the method.driver from imported class else no output
print(act)
driver.close()
if act == 'Dashboard / nopCommerce administration':
    assert True

else:
    assert False
