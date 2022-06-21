"""
----------------------------------------------------------------------------------------------------------
Description:

usage: This class is being used to locate all possible web elements

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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.helper_classes.web_element_waiters import Waiter
import sys
import pyautogui
# import win32com.client
import time


waiter = Waiter()
# pyautogui.FAILSAFE = False


class LocatePageElements:
    @staticmethod
    def send_keys_element(driver, obj, value):
        """
        This method is being used to send some input to the test field
        :param driver: selenium driver
        :param obj: locator details
        :param value: value to be passed as an input
        :return: None
        """
        try:
            waiter.explicit_waiter(driver, obj[0], obj[1])
            driver.find_element(obj[0], obj[1]).clear()
            driver.find_element(obj[0], obj[1]).send_keys(value)
        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            # print("Exception message: {}".format(exception))
            print("Relevant Locators: ", obj[1])
            # sys.exit(1)

    @staticmethod
    def send_keys_element_in_multi_div(driver, obj, value, div_count=2):
        """
        This method is being used to send some input to the test field
        :param div_count:
        :param driver: selenium driver
        :param obj: locator details
        :param value: value to be passed as an input
        :return: None
        """
        try:
            print(obj[1].replace('COUNT', str(div_count)))
            print(value)
            waiter.explicit_waiter(driver, obj[0], obj[1].replace('COUNT', str(div_count)))
            # driver.find_element(obj[0], obj[1].replace('COUNT', str(div_count))).clear()
            enter_value = driver.find_element(obj[0], obj[1].replace('COUNT', str(div_count)))
            enter_value.send_keys(value)
        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            # print("Exception message: {}".format(exception))
            print("Relevant Locators: ", obj[1])
            # sys.exit(1)

    @staticmethod
    def send_keys_by_enter(driver, obj, value):
        """
        This method is being used to send some input to the test field by click on the field first
        :param driver: selenium driver
        :param obj: locator details
        :param value: value to be passed as an input
        :return: None
        """
        try:
            driver = driver
            waiter.explicit_waiter(driver, obj[0], obj[1])
            # driver.find_element(obj[0], obj[1]).clear()
            driver.find_element(obj[0], obj[1]).send_keys(value, Keys.ENTER)
        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            # print("Exception message: {}".format(exception))
            print("Relevant Locators: ", obj[1])
            # sys.exit(1)

    @staticmethod
    def click_and_enter(driver, obj, value=''):
        """
        This method is being used to send some input to the test field by click on the field first
        :param driver: selenium driver
        :param obj: locator details
        :param value: value to be passed as an input
        :return: None
        """
        try:
            driver = driver
            waiter.explicit_waiter(driver, obj[0], obj[1])
            # driver.find_element(obj[0], obj[1]).clear()
            driver.find_element(obj[0], obj[1]).click()
        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            # print("Exception message: {}".format(exception))
            print("Relevant Locators: ", obj[1])
            # sys.exit(1)

    @staticmethod
    def click_and_enter_2(driver, obj):
        try:
            driver = driver
            waiter.explicit_waiter(driver, obj[0], obj[1])
            driver.find_element(obj[0], obj[1]).send_keys(Keys.RETURN)
        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            # print("Exception message: {}".format(exception))
            print("Relevant Locators: ", obj[1])
            # sys.exit(1)

    @staticmethod
    def click_elements(driver, obj):
        """
        This is being used to click any web element
        :param driver: selenium driver
        :param obj: locators details
        :return: None
        """
        try:
            waiter.explicit_waiter_for_click(driver, obj[0], obj[1])
            driver.find_element(obj[0], obj[1]).click()
            return True
        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            # print("Exception message: {}".format(exception))
            print("Relevant Locators: ", obj[1])
            return False
            # sys.exit(1)

    @staticmethod
    def hover_and_click_elements(driver, obj):
        """
        This is being used to click any web element
        :param driver: selenium driver
        :param obj: locators details
        :return: None
        """
        try:
            waiter.explicit_waiter_for_click(driver, obj[0], obj[1])
            button = driver.find_element_by_xpath(obj[1])
            driver.execute_script("arguments[0].click();", button)
        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            # print("Exception message: {}".format(exception))
            print("Relevant Locators: ", obj[1])
            # sys.exit(1)

    @staticmethod
    def on_hover_and_click_checkbox(driver, obj):
        """
        This is being used to click any web element
        :param driver: selenium driver
        :param obj: locators details
        :return: None
        """
        try:
            waiter.explicit_waiter_for_click(driver, obj[0], obj[1])
            element_to_hover_over = driver.find_element_by_xpath(obj[1])
            actions = ActionChains(driver)
            actions.move_to_element(element_to_hover_over)
            time.sleep(3)
            actions.click()
            actions.perform()
        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            # print("Exception message: {}".format(exception))
            print("Relevant Locators: ", obj[1])
            # sys.exit(1)

    @staticmethod
    def click_elements_by_Scrape_data(driver, obj):
        """
        This method is being used to click on any element by scraping the data first
        :param driver: selenium driver
        :param obj: locator list
        :return: None
        """
        try:
            waiter.explicit_waiter_for_click(driver, obj[0], obj[1])
            driver.find_element(obj[0], obj[1]).click()
        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            # print("Exception message: {}".format(exception))
            print("Relevant Locators: ", obj[1])
            # sys.exit(1)

    @staticmethod
    def date_picker(driver, obj_date_field, obj_date_picker, date_value):

        """
        This method is being used to add date in calendar
        :param driver: selenium driver
        :param obj_date_field: locator info for date field
        :param obj_date_picker: locator info for date picker
        :param date_value: date to be passed to locator
        :return: None
        """
        try:
            try:
                waiter.explicit_waiter_for_click(driver, obj_date_field[0], obj_date_field[1])
                driver.find_element(obj_date_field[0], obj_date_field[1]).click()
            except:
                waiter.explicit_waiter_for_click(driver, obj_date_field[0], obj_date_field[1])
                button = driver.find_element_by_xpath(obj_date_field[1])
                driver.execute_script("arguments[0].click();", button)
            try:
                time.sleep(3)
                waiter.explicit_waiter_for_click(driver, obj_date_picker[0],
                                                 obj_date_picker[1].replace("DD", date_value))
                driver.find_element(obj_date_picker[0], obj_date_picker[1].replace("DD", date_value)).click()
            except:
                time.sleep(2)
                waiter.explicit_waiter_for_click(driver, obj_date_picker[0],
                                                 obj_date_picker[1].replace("DD", date_value))
                button = driver.find_element_by_xpath(obj_date_picker[1].replace("DD", date_value))
                driver.execute_script("arguments[0].click();", button)
        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            # print("Exception message: {}".format(exception))
            # sys.exit(1)

    @staticmethod
    def set_toggle_false(driver, obj):
        """
        Method is being used to set the toggle option
        :param driver: selenium driver
        :param obj: locator info
        :return: None
        """
        try:
            elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, obj[1])))
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView();", elem)
            time.sleep(1)
            elem.click()
        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            # print("Exception message: {}".format(exception))
            print("Relevant Locators: ", obj[1])
            # sys.exit(1)

    @staticmethod
    def get_element_text(driver, obj, waiter_time=20):
        """
        This method is being used to get the text from any web object
        :param driver: selenium driver
        :param obj: locator info
        :return: alert text
        """
        try:
            waiter.explicit_waiter(driver, obj[0], obj[1], waiter_time)
            alert_msg = driver.find_element(obj[0], obj[1])
            return alert_msg.text
        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            # print("Exception message: {}".format(exception))
            print("Relevant Locators: ", obj[1])
            # sys.exit(1)

    @staticmethod
    def get_element_text_without_wait(driver, obj):
        """
        This method is being used to get the text from any web object
        :param driver: selenium driver
        :param obj: locator info
        :return: alert text
        """
        try:
            driver.implicitly_wait(0)
            alert_msg = driver.find_element(obj[0], obj[1])
            return alert_msg.text
        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            # print("Exception message: {}".format(exception))
            print("Relevant Locators: ", obj[1])
            # sys.exit(1)

    @staticmethod
    def get_dynamic_alert_message(driver, obj, entity_name):
        """
        This helps to get the text from alert messages
        :param driver: selenium driver
        :param obj: Locator Info
        :param entity_name: this would be the name of visitor/employee/contractor etc.
        :return: alert text
        """
        try:
            waiter.explicit_waiter(driver, obj[0], obj[1].replace("VisitorName", entity_name))
            alert_msg = driver.find_element(obj[0], obj[1].replace("VisitorName", entity_name))
            return alert_msg.text
        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            # print("Exception message: {}".format(exception))
            print("Relevant Locators: ", obj[1])
            # sys.exit(1)

    @staticmethod
    def get_to_specific_url(driver, url):
        """
        this is being used to navigate to the specific URL
        :param driver: Selenium driver
        :param url: Specific URL
        :return: None
        """
        driver.get(url)

    @staticmethod
    def find_web_element_only(driver, locator_obj):
        """
        This is being used to locate the web element only
        :param driver: selenium driver
        :param locator_obj: web locator
        :return: Boolean value
        """
        try:
            waiter.explicit_waiter(driver, locator_obj[0], locator_obj[1])
            if driver.find_element(locator_obj[0], locator_obj[1]):
                return True
            else:
                return False
        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            # print("Exception message: {}".format(exception))
            print("Relevant Locators: ", locator_obj[1])
            # sys.exit(1)

    @staticmethod
    def scroll_down_web_page(driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return None

    @staticmethod
    def switch_to_child_tab(driver):
        driver.switch_to.window(driver.window_handles[1])
        return None

    @staticmethod
    def switch_to_parent_tab(driver):
        driver.switch_to.window(driver.window_handles[0])
        return None

    @staticmethod
    def get_element_attribute_value(driver, locator_object, attr_name):
        try:
            waiter.explicit_waiter(driver, locator_object[0], locator_object[1])
            dom = driver.find_element(locator_object[0], locator_object[1])
            attr_value = dom.get_attribute(attr_name)
            return attr_value
        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            # print("Exception message: {}".format(exception))
            print("Relevant Locators: ", locator_object[1])
            # sys.exit(1)

    @staticmethod
    def close_tab(driver):
        driver.close()
        return None

    @staticmethod
    def accept_confirmation_alert(driver):
        try:
            try:
                waiter.waiter_for_alerts(driver)
                driver.switchTo().alert().accept()
            except:
                waiter.waiter_for_alerts(driver)
                alert = driver.switch_to.alert
                alert.accept()
        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            # print("Exception message: {}".format(exception))
            # sys.exit(1)

    @staticmethod
    def attach_document_from_window_browser(driver, file_path):
        # try:
        pyautogui.FAILSAFE = False
        time.sleep(3)  # waiting for window popup to open
        pyautogui.write(file_path)  # path of File
        time.sleep(4)
        pyautogui.press('enter')
        time.sleep(3)
        # driver.switch_to.frame(0)
        # except KeyboardInterrupt:
        #     sys.exit()

    @staticmethod
    def drag_drop_element(driver, obj_drag, obj_drop):
        driver.switch_to.frame(0)
        drag_element = driver.find_element_by_xpath(obj_drag[1])
        drop_element = driver.find_element_by_xpath(obj_drop[1])
        ActionChains(driver).drag_and_drop(drag_element, drop_element).perform()
        time.sleep(60)


