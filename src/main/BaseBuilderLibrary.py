import sys
import os
from Selenium2Library import Selenium2Library
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class BaseBuilderLibrary(object):
    platform_name = None
    browser_name = None
    browser_path = None

    def __init__(self, browser_name):
        self.browser_name = browser_name
        self.result = ''

    def get_platform(self):
        self.platform_name = sys.platform
        self.browser_path = os.getcwd()
        return self.platform_name

    # def set_browser(self, browser_name):
    #     self.browser_name = browser_name

    def set_browser_path(self, urlSite):
        self.get_platform()
        if self.platform_name =='darwin':
            webdriver.Chrome(executable_path=self.browser_path + '/driver/mac/chromedriver')
            Selenium2Library().open_browser(browser='chrome', url = urlSite)
        elif self.platform_name == 'win32':
            self.browser_path = '..src/resources/windows/chromedriver'
            print(self.browser_path)
        else:
            self.browser_path = '..src/resources/linux/chromedriver'
            print(self.browser_path)