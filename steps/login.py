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

from page_model.login import Login, LoginLocators
from steps.home import screenshot

use_step_matcher('re')


@step('I enter "(.*)" into the "(.*)" field')
def step_impl(context, text, field):
    page = Login(context.driver)
    wait = WebDriverWait(context.driver, 3)

    try:
        wait.until(EC.element_to_be_clickable(LoginLocators.login_field(field)))
        page.login_field(field).send_keys(text)
    except (NoSuchElementException, TimeoutException, StaleElementReferenceException, AssertionError) as e:
        screenshot(context)
        raise e


@step('I click the submit button')
def step_impl(context):
    page = Login(context.driver)
    wait = WebDriverWait(context.driver, 3)

    try:
        wait.until(EC.element_to_be_clickable(LoginLocators.SUBMIT_BUTTON))
        page.submit_button().click()
    except (NoSuchElementException, TimeoutException, StaleElementReferenceException, AssertionError) as e:
        screenshot(context)
        raise e


@step('I verify that the error message displays')
def step_impl(context):
    page = Login(context.driver)
    wait = WebDriverWait(context.driver, 3)

    try:
        wait.until(EC.element_to_be_clickable(LoginLocators.LOGIN_ERROR_MESSAGE))
        assert page.login_error_message()
    except (NoSuchElementException, TimeoutException, StaleElementReferenceException, AssertionError) as e:
        screenshot(context)
        raise e