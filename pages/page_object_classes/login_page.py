"""
----------------------------------------------------------------------------------------------------------
Description:

usage: click_on_login pages

Author  : Usman Zahid
Release : 1

Modification Log:

-----------------------------------------------------------------------------------------------------------
Date                Author              Story               Description
-----------------------------------------------------------------------------------------------------------
21/06/2022        Usman Zahid                             Initial draft.
-----------------------------------------------------------------------------------------------------------

"""
import time
from pages.locators.login_module import StagingEnv, SandboxEnv, ProdEnv
from pages.page_elements.locate_elements import LocatePageElements

base_elements = LocatePageElements()
login_page_staging = StagingEnv()
login_page_sandbox = SandboxEnv()
login_page_prod = ProdEnv()


class LoginPage:
    @staticmethod
    def add_username(driver, value, env):
        if env == 'staging':
            base_elements.send_keys_element(driver, login_page_staging.username, value)
        elif env == 'sandbox':
            base_elements.send_keys_element(driver, login_page_sandbox.username, value)
        elif env == 'prod':
            base_elements.send_keys_element(driver, login_page_prod.username, value)

    @staticmethod
    def add_password(driver, value, env):
        if env == 'staging':
            base_elements.send_keys_element(driver, login_page_staging.password, value)
        elif env == 'sandbox':
            base_elements.send_keys_element(driver, login_page_sandbox.password, value)
        elif env == 'prod':
            base_elements.send_keys_element(driver, login_page_prod.password, value)

    @staticmethod
    def click_on_login(driver, env):
        if env == 'staging':
            base_elements.click_elements(driver, login_page_staging.login_btn)
        elif env == 'sandbox':
            base_elements.click_elements(driver, login_page_sandbox.login_btn)
        elif env == 'prod':
            base_elements.click_elements(driver, login_page_prod.login_btn)

    @staticmethod
    def get_dashboard_title(driver, env):
        if env == 'staging':
            is_dashboard_found = base_elements.get_element_text(driver, login_page_staging.dashboard_title)
            return is_dashboard_found
        elif env == 'sandbox':
            is_dashboard_found = base_elements.get_element_text(driver, login_page_sandbox.dashboard_title)
            return is_dashboard_found
        elif env == 'prod':
            is_dashboard_found = base_elements.get_element_text(driver, login_page_prod.dashboard_title)
            return is_dashboard_found

    @staticmethod
    def click_menu_button(driver, env):
        if env == 'staging':
            base_elements.click_elements(driver, login_page_staging.click_on_menu_btn)
        elif env == 'sandbox':
            base_elements.click_elements(driver, login_page_sandbox.click_on_menu_btn)
        elif env == 'prod':
            base_elements.click_elements(driver, login_page_prod.click_on_menu_btn)

    @staticmethod
    def click_on_logout_btn(driver, env):
        if env == 'staging':
            is_user_logout = base_elements.click_elements(driver, login_page_staging.click_on_logout_button)
            return is_user_logout
        elif env == 'sandbox':
            is_user_logout = base_elements.click_elements(driver, login_page_sandbox.click_on_logout_button)
            return is_user_logout
        elif env == 'prod':
            is_user_logout = base_elements.click_elements(driver, login_page_prod.click_on_logout_button)
            return is_user_logout

    @staticmethod
    def get_error_message_while_login_without_credentials(driver, env):
        if env == 'staging':
            validate_text = base_elements.get_element_text(driver,
                                                           login_page_staging.validate_mandatory_field_message_for_email)
            return validate_text
        elif env == 'sandbox':
            validate_text = base_elements.get_element_text(driver, login_page_sandbox.
                                                           validate_mandatory_field_message_for_email)
            return validate_text
        elif env == 'prod':
            validate_text = base_elements.get_element_text(driver, login_page_prod.
                                                           validate_mandatory_field_message_for_email)
            return validate_text

    @staticmethod
    def close_error_message(driver, env):
        if env == 'staging':
            close_error_message = base_elements.click_elements(driver, login_page_staging.close_error_message)
            return close_error_message
        elif env == 'sandbox':
            close_error_message = base_elements.click_elements(driver, login_page_sandbox.close_error_message)
            return close_error_message
        elif env == 'prod':
            close_error_message = base_elements.click_elements(driver, login_page_prod.close_error_message)
            return close_error_message

    @staticmethod
    def get_error_message_while_login_with_invalid_password(driver, env):
        if env == 'staging':
            validate_text = base_elements.get_element_text(driver,
                                                           login_page_staging.validate_mandatory_field_message_for_email)
            return validate_text
        elif env == 'sandbox':
            validate_text = base_elements.get_element_text(driver, login_page_sandbox.
                                                           validate_mandatory_field_message_for_email)
            return validate_text
        elif env == 'prod':
            validate_text = base_elements.get_element_text(driver, login_page_prod.
                                                           validate_mandatory_field_message_for_email)
            return validate_text

    @staticmethod
    def get_error_message_while_login_with_locked_user(driver, env):
        if env == 'staging':
            validate_text = base_elements.get_element_text(driver,
                                                           login_page_staging.validate_mandatory_field_message_for_email)
            return validate_text
        elif env == 'sandbox':
            validate_text = base_elements.get_element_text(driver, login_page_sandbox.
                                                           validate_mandatory_field_message_for_email)
            return validate_text
        elif env == 'prod':
            validate_text = base_elements.get_element_text(driver, login_page_prod.
                                                           validate_mandatory_field_message_for_email)
            return validate_text

    @staticmethod
    def identify_problem_in_dashboard_for_problem_user(driver, env):
        if env == 'staging':
            is_problem_found = base_elements.get_element_text(driver, login_page_staging.get_problem_identifier_for_problem_user)
            return is_problem_found
        elif env == 'sandbox':
            is_problem_found = base_elements.get_element_text(driver, login_page_sandbox.get_problem_identifier_for_problem_user)
            return is_problem_found
        elif env == 'prod':
            is_problem_found = base_elements.get_element_text(driver, login_page_prod.get_problem_identifier_for_problem_user)
            return is_problem_found

    @staticmethod
    def get_login_delayed_time(driver, env):
        if env == 'staging':
            is_dashboard_found = base_elements.get_element_text_without_wait(driver, login_page_staging.dashboard_title)
        elif env == 'sandbox':
            is_dashboard_found = base_elements.get_element_text_without_wait(driver, login_page_sandbox.dashboard_title)
        elif env == 'prod':
            is_dashboard_found = base_elements.get_element_text_without_wait(driver, login_page_prod.dashboard_title)
        return time.time()

# print(time.time())
# print(time.time())
# login_start_time = time.time()
# loin_end_time = time.time()