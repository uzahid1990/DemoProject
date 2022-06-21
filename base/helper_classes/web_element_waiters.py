"""
----------------------------------------------------------------------------------------------------------
Description:

usage: Waiter class for locating web elements

Author  : Usman Zahid
Release : 1

Modification Log:

-----------------------------------------------------------------------------------------------------------
Date                Author              Story               Description
-----------------------------------------------------------------------------------------------------------
21/06/2022        Usman Zahid                             Initial draft.
-----------------------------------------------------------------------------------------------------------

"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class Waiter:

    @staticmethod
    def explicit_waiter(driver, locator_type, locator_obj, waiter_time=20):
        """
        This method is being used to apply explicit wait on find element
        :param driver: webdriver
        :param locator_type: locator type to be xpath, class, name, id etc.
        :param locator_obj: Value of locator
        :return: None
        """
        try:
            if locator_type == "xpath":
                WebDriverWait(driver, waiter_time).until(EC.presence_of_element_located(
                    (By.XPATH, locator_obj)))
            elif locator_type == "css":
                WebDriverWait(driver, waiter_time).until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, locator_obj)))
        except Exception as e:
            print("Locator not found: ", locator_obj, e)

    @staticmethod
    def explicit_waiter_for_click(driver, locator_type, locator_obj):
        """
        This method is being used to apply explicit wait on find element
        :param driver: webdriver
        :param locator_type: locator type to be xpath, class, name, id etc.
        :param locator_obj: Value of locator
        :return: None
        """
        try:
            if locator_type == "xpath":
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, locator_obj)))
        except Exception as e:
            print("Locator not found: ", locator_obj, e)

    @staticmethod
    def explicit_waiter_for_toggle(driver, locator_type, locator_obj):
        """
        This waiter is being used for toggle setup
        :param driver: webdriver driver
        :param locator_type: locator type
        :param locator_obj: value of locator
        :return:
        """
        try:
            if locator_type == "xpath":
                elm = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                    (By.XPATH, locator_obj)))
                return elm
        except Exception as e:
            print("Locator not found: ", locator_obj, e)

    @staticmethod
    def waiter_for_alerts(driver, waiter_time=10):
        try:
            WebDriverWait(driver, waiter_time).until(EC.alert_is_present())
        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            print("Exception message: {}".format(exception))
