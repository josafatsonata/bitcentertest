import os.path
import time

from pytz import timezone
import datetime
import sys
from random import randint
from behave import *
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from properties import Properties

from page_model.home_page import HomePage, HomePageLocators

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    chrome_options = Options()
    if sys.platform == 'win32':
        chrome_options.add_argument("--start-maximized")
    else:
        chrome_options.add_argument("--kiosk")

    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-infobars")
    context.driver = webdriver.Chrome(Properties.select_driver(), chrome_options=chrome_options)

    page = HomePage(context.driver)
    context.driver.get(page.url)


@When('I click the login button in the home page')
def step_impl(context):
    page = HomePage(context.driver)
    wait = WebDriverWait(context.driver, 3)

    try:
        wait.until(EC.element_to_be_clickable(HomePageLocators.LOGIN))
        page.login_button().click()
    except (NoSuchElementException, TimeoutException, StaleElementReferenceException, AssertionError) as e:
        screenshot(context)
        raise e


@then('I wait "(.*)" seconds')
def step_impl(context, period):
    time.sleep(int(period))


@step('I close the browser')
def step_impl(context):
    context.driver.quit()


def screenshot(context):
    current_date = str(datetime.datetime.now().astimezone(timezone('US/Pacific')))[0:19]
    current_date = current_date.replace(':', '-')
    platforms = {
        'linux': '/',
        'darwin': '/',
        'win32': '\\'
    }
    path = os.path.dirname(os.path.abspath(__file__))[:-5] + "screenshots" + platforms[sys.platform]
    context.driver.save_screenshot(path + str(context.scenario.name)[0:11] + current_date + ".png")