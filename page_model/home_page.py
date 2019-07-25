from locators.home_page import HomePageLocators
from page_model.base_page import BasePage


class HomePage(BasePage):
    @property
    def url(self):
        return super(HomePage, self).url + '/'

    def login_button(self):
        return self.driver.find_element(*HomePageLocators.LOGIN)
