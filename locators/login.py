from selenium.webdriver.common.by import By


class LoginLocators:
    SUBMIT_BUTTON = By.XPATH, "//button[@type='submit']"
    LOGIN_ERROR_MESSAGE = By.XPATH, "//div[@class='notices is-bottom']"

    @staticmethod
    def login_field(field):
        """

        :param field: email or password
        :return: email or password field
        """
        return By.XPATH, f"//input[@name='{field}']"

"""
//input[@name='email']
//input[@name='password']


"""