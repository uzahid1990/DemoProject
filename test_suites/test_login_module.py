"""
----------------------------------------------------------------------------------------------------------
Description:

usage: This test suite contains all possible test cases of login module from demo application

Author  : Usman Zahid
Release : 1

Modification Log:

-----------------------------------------------------------------------------------------------------------
Date                Author              Story               Description
-----------------------------------------------------------------------------------------------------------
21/06/2022        Usman Zahid                             Initial draft.
-----------------------------------------------------------------------------------------------------------

"""

from pages.page_object_classes.setup import Setup
from pages.page_object_classes.login_page import LoginPage
from base.helper_classes.json_parser import ReadJson
from base.helper_classes.generate_file_path import GetFileName
import pytest
import os
import time

"""------------Global Classes Objects-------------"""
setup_class = Setup()
login = LoginPage()
json_class_object = ReadJson()
file_name_obj = GetFileName()


"---------------------------------Generating File Path For All Environments-------------------------------------"


def get_file_path(environment):
    """
    This function specific suit function which is being used to get the configuration file path based on the given
    Env, this will be used in all the suits
    :param environment: Environment, on which the test will be conducted
    :return: Config File Path
    """
    cur_path = os.path.dirname(__file__)
    config_json_path = os.path.relpath('../resources/configurations/' + file_name_obj.get_file_name(environment),
                                       cur_path)
    return config_json_path


"--------------------------------Global variables for this test suits-----------------------------------"
driver = ''


"---------------------------------Params for Pytest Fixture-------------------------------------"


def get_params():
    """
    This function is being used to iterate the test cases with respect to the given browsers
    :return: browser list
    """
    param_obj = {"browser": ["chrome", "firefox"]}
    return " "  # param_obj["browser"]


@pytest.fixture(params=get_params())
def params(request):
    """
    Fixture is applied to execute test cases dynamically for multiple attributes
    :param request:
    :return: This will return the params from side_by_side_execution_config file and keep itself to execute test cases
    one by one
    """
    return request.param


"*****************************Test Cases*****************************"


@pytest.mark.parametrize(
    "test_name",
    [
        " Validate the application URL is being opened  ",
    ],
    ids=['Validate the application URL is being opened']
)
def test_lg_01(params, envs, is_headless, test_name):
    """Login Module"""
    json_obj = json_class_object.read_config_json(get_file_path(envs))
    driver_obj = setup_class.setup(json_obj["base_url"], header_less=is_headless)
    global driver
    driver = driver_obj


@pytest.mark.parametrize(
    "test_name",
    [
        " Validate the user is being logged in successfully  ",
    ],
    ids=['Validate the user is being logged in successfully']
)
def test_lg_02(params, envs, test_name):
    """Login Module"""
    json_obj = json_class_object.read_config_json(get_file_path(envs))
    login.add_username(driver, json_obj["base_credentials"]["user_name"], envs)
    login.add_password(driver, json_obj["base_credentials"]["password"], envs)
    login.click_on_login(driver, envs)
    dashboard_title = login.get_dashboard_title(driver, envs)
    assert dashboard_title == 'PRODUCTS'


@pytest.mark.parametrize(
    "test_name",
    [
        " Validate the user is being logout successfully  ",
    ],
    ids=['Validate the user is being logout successfully']
)
def test_lg_03(params, envs, test_name):
    """Login Module"""
    login.click_menu_button(driver, envs)
    logout = login.click_on_logout_btn(driver, envs)
    assert logout is True


@pytest.mark.parametrize(
    "test_name",
    [
        " Validate the user is not able to login without credentials",
    ],
    ids=['Validate the user is not able to login without credentials']
)
def test_lg_04(params, envs, test_name):
    """Login Module"""
    login.click_on_login(driver, envs)
    error_message = login.get_error_message_while_login_without_credentials(driver, envs)
    assert error_message == "Epic sadface: Username is required"


@pytest.mark.parametrize(
    "test_name",
    [
        " Validate the error message is being closed upon clicking on cross button",
    ],
    ids=['Validate the error message is being closed upon clicking on cross button']
)
def test_lg_05(params, envs, test_name):
    """Login Module"""
    close_error_message = login.close_error_message(driver, envs)
    assert close_error_message is True


@pytest.mark.parametrize(
    "test_name",
    [
        " Validate the user is restricted to login with invalid password",
    ],
    ids=['Validate the user is restricted to login with invalid password']
)
def test_lg_06(params, envs, test_name):
    """Login Module"""
    json_obj = json_class_object.read_config_json(get_file_path(envs))
    login.add_username(driver, json_obj["base_credentials"]["user_name"], envs)
    login.add_password(driver, "thisInvalidPWD", envs)
    login.click_on_login(driver, envs)
    error_message = login.get_error_message_while_login_with_invalid_password(driver, envs)
    assert error_message == "Epic sadface: Username and password do not match any user in this service"


@pytest.mark.parametrize(
    "test_name",
    [
        " Validate the user is restricted to login with with locked user credentials",
    ],
    ids=['Validate the user is restricted to login with with locked user credentials']
)
def test_lg_07(params, envs, test_name):
    """Login Module"""
    json_obj = json_class_object.read_config_json(get_file_path(envs))
    login.add_username(driver, "locked_out_user", envs)
    login.add_password(driver, json_obj["base_credentials"]["password"], envs)
    login.click_on_login(driver, envs)
    error_message = login.get_error_message_while_login_with_locked_user(driver, envs)
    assert error_message == "Epic sadface: Sorry, this user has been locked out."


@pytest.mark.parametrize(
    "test_name",
    [
        " Validate there should no any problem while login to the dashboard",
    ],
    ids=['Validate there should no any problem while login to the dashboard']
)
def test_lg_08(params, envs, test_name):
    """Login Module"""
    json_obj = json_class_object.read_config_json(get_file_path(envs))
    login.add_username(driver, "problem_user", envs)
    login.add_password(driver, json_obj["base_credentials"]["password"], envs)
    login.click_on_login(driver, envs)
    problem_identifier = login.identify_problem_in_dashboard_for_problem_user(driver, envs)
    login.click_menu_button(driver, envs)
    login.click_on_logout_btn(driver, envs)
    assert problem_identifier != "Sauce Labs Backpack"


@pytest.mark.parametrize(
    "test_name",
    [
        " Validate there should no any delay while login to the application",
    ],
    ids=['Validate there should no any delay while login to the application']
)
def test_lg_09(params, envs, test_name):
    """Login Module"""
    json_obj = json_class_object.read_config_json(get_file_path(envs))
    login.add_username(driver, "performance_glitch_user", envs)
    login.add_password(driver, json_obj["base_credentials"]["password"], envs)
    login_start_time = time.time()
    login.click_on_login(driver, envs)
    login_end_time = login.get_login_delayed_time(driver, envs)
    login_time = login_end_time - login_start_time
    assert login_time == 1


def test_lg_tearDown():
    """Login Module"""
    time.sleep(1)
    driver.quit()
