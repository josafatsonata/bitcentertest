from page_model.base_page import BasePage
from locators.login import LoginLocators


class Login(BasePage):
    def login_url(self):
        return super(Login, self).url + '/login'

    def submit_button(self):
        return self.driver.find_element(*LoginLocators.SUBMIT_BUTTON)

    def login_field(self, field):
        return self.driver.find_element(*LoginLocators.login_field(field))

    def login_error_message(self):
        return self.driver.find_element(*LoginLocators.LOGIN_ERROR_MESSAGE)
