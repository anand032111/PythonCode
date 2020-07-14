class HomePage():

    def __init__(self,driver):
        self.driver = driver

        self.account_link_xpath ="//span[@id='account-job']//i"
        self.logout_button_id ="logoutLink"

    def click_account(self):
        self.driver.find_element_by_xpath(self.account_link_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_id(self.logout_button_id).click()
