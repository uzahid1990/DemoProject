"""
----------------------------------------------------------------------------------------------------------
Description:

usage: setup class for initializing the browser

Author  : Usman Zahid
Release : 1

Modification Log:

-----------------------------------------------------------------------------------------------------------
Date                Author              Story               Description
-----------------------------------------------------------------------------------------------------------
22/12/2021        Usman Zahid                             Initial draft.
-----------------------------------------------------------------------------------------------------------

"""

from selenium import webdriver
from pages.page_elements.locate_elements import LocatePageElements
from selenium.webdriver.chrome.options import Options


class Setup:
    @staticmethod
    def setup(url, header_less=True):
        # Initializing the Chrome Driver
        options = Options()
        options.headless = header_less
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        # connecting with URL
        driver.get(url)
        return driver
