class StagingEnv:
    """******************************************************************************************
                                        Login
    ******************************************************************************************"""
    username = ['xpath', '//input[@id="user-name"]']
    password = ['xpath', '//input[@id="password"]']
    login_btn = ['xpath', '//*[@name="login-button"]']
    dashboard_title = ['xpath', '//*[@class="title"]']
    click_on_menu_btn = ['xpath', '//*[@id="react-burger-menu-btn"]']
    click_on_logout_button = ['xpath', '//*[@id="logout_sidebar_link"]']
    validate_mandatory_field_message_for_email = ['xpath', '//h3[@data-test="error"]']
    close_error_message = ['xpath', '//*[@class="error-button"]']
    invalid_password_error = ['xpath', '//h3[@data-test="error"]']
    locked_user_error = ['xpath', '//h3[@data-test="error"]']
    get_problem_identifier_for_problem_user = ['xpath', '//a[@id="item_4_title_link"]//child::div[1]']


class SandboxEnv:
    """******************************************************************************************
                                        Login
    ******************************************************************************************"""
    username = ['xpath', '//input[@id="user-name"]']
    password = ['xpath', '//input[@id="password"]']
    login_btn = ['xpath', '//*[@name="login-button"]']
    dashboard_title = ['xpath', '//*[@class="title"]']
    click_on_menu_btn = ['xpath', '//*[@id="react-burger-menu-btn"]']
    click_on_logout_button = ['xpath', '//*[@id="logout_sidebar_link"]']
    validate_mandatory_field_message_for_email = ['xpath', '//h3[@data-test="error"]']
    close_error_message = ['xpath', '//*[@class="error-button"]']
    invalid_password_error = ['xpath', '//h3[@data-test="error"]']
    locked_user_error = ['xpath', '//h3[@data-test="error"]']
    get_problem_identifier_for_problem_user = ['xpath', '//a[@id="item_4_title_link"]//child::div[1]']


class ProdEnv:
    """******************************************************************************************
                                        Login
    ******************************************************************************************"""
    username = ['xpath', '//input[@id="user-name"]']
    password = ['xpath', '//input[@id="password"]']
    login_btn = ['xpath', '//*[@name="login-button"]']
    dashboard_title = ['xpath', '//*[@class="title"]']
    click_on_menu_btn = ['xpath', '//*[@id="react-burger-menu-btn"]']
    click_on_logout_button = ['xpath', '//*[@id="logout_sidebar_link"]']
    validate_mandatory_field_message_for_email = ['xpath', '//h3[@data-test="error"]']
    close_error_message = ['xpath', '//*[@class="error-button"]']
    invalid_password_error = ['xpath', '//h3[@data-test="error"]']
    locked_user_error = ['xpath', '//h3[@data-test="error"]']
    get_problem_identifier_for_problem_user = ['xpath', '//a[@id="item_4_title_link"]//child::div[1]']


