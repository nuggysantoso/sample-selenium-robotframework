import os
import sys
from robot.libraries.BuiltIn import BuiltIn
from Selenium2Library import Selenium2Library
from selenium import webdriver
from SeleniumLibrary.utils import (is_falsy, is_noney, is_truthy, plural_or_not as s)
from robot.api import logger
from SeleniumLibrary.base import LibraryComponent, keyword
from selenium.webdriver.common.keys import Keys

class BaseDriverBuilder(object):
    platform_name   = None
    browser_name    = None
    browser_path    = None
    driver          = None

    def get_platform(self):
        self.platform_name = sys.platform
        self.browser_path = os.path.dirname(os.getcwd())
        return self.platform_name

    def get_browser_path(self):
        browser_directory = None
        self.get_platform()
        if self.platform_name == 'darwin':
            if "chrome" in self.get_browser_name().lower():
                browser_directory = self.browser_path + "/test/resources/driver/mac/chromedriver"
        elif self.platform_name == 'win32':
            if "chrome" in self.get_browser_name().lower():
                browser_directory = self.browser_path + "/test/resources/driver/windows/chromedriver"
        else:
            if "chrome" in self.get_browser_name().lower():
                browser_directory = self.browser_path + "/test/resources/driver/linux/chromedriver"
        return browser_directory

    def set_browser_name(self, browser_name):
        self.browser_name = browser_name

    def get_browser_name(self):
        return self.browser_name

    def open_window_browser(self, urlSite):
        self.driver = webdriver.Chrome(executable_path=self.get_browser_path())
        self.driver.get(urlSite)
        self.driver.maximize_window()

    def close_all_browser(self):
        self.driver.quit()

    def element_should_visible_by_id(self, locator, messages=None):
        element = self.driver.find_element_by_id(str(locator))
        if not element.is_displayed():
            if is_noney(messages):
                messages = ("Failed : element is not displayed by id '%s'" %locator)
            raise AssertionError(messages)

    def element_should_visible_by_xpath(self, locator, messages=None):
        element = self.driver.find_element_by_xpath(str(locator))
        assert element.is_displayed()

    def element_should_visible_by_class(self, locator, messages=None):
        element = self.driver.find_element_by_class_name(str(locator))
        assert element.is_displayed()

    def element_should_visible_by_css_selector(self, locator, messages=None):
        element = self.driver.find_element_by_css_selector(str(locator))
        assert element.is_displayed()

    def element_should_visible_by_name(self, locator, messages=None):
        element = self.driver.find_element_by_name(str(locator))
        assert element.is_displayed()

    def element_should_visible_by_tag_name(self, locator, messages=None):
        element = self.driver.find_element_by_tag_name(str(locator))
        assert element.is_displayed()

    def element_should_visible_by_link_text(self, locator, messages=None):
        element = self.driver.find_element_by_link_text(str(locator))
        assert element.is_displayed()

    def element_should_visible_by_partial_link_text(self, locator, messages=None):
        element = self.driver.find_element_by_partial_link_text(str(locator))
        assert element.is_displayed()

    def click_element_by_id(self, locator):
        element = self.driver.find_element_by_id(str(locator))
        element.click()
    