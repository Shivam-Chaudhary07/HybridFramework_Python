class Login:
    textbox_username_id = 'Email'
    textbox_password_id = "Password"
    button_login_xpath = '//*[@type = "submit"]'
    link_logout_linktext = 'Logout'

    def __init__(self, driver):
        self.driver = driver

    def enterUsername(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
        #we use self.variable name bcz these variables belong to a class

    def enterPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()