import sys
import os

class BaseBuilderLibrary(object):
    platform_name = None
    browser_name = None
    browser_path = None

    def __init__(self):
        self.result = ''

    def get_platform(self):
        self.platform_name = sys.platform
        return self.platform_name

    def set_browser(self, browser_name):
        self.browser_name = browser_name

    def set_browser_path(self):
        self.get_platform()
        if self.platform_name =='darwin':
            if self.browser_name == 'Chrome':
                self.browser_path = '..src/resources/mac/chromedriver'
                print(self.browser_path)
            else:
                self.browser_path = '..src/resources/mac/geckodriver'
                print(self.browser_path)
        elif self.platform_name == 'win32':
            if self.browser_name == 'Chrome':
                self.browser_path = '..src/resources/windows/chromedriver'
                print(self.browser_path)
            else:
                self.browser_path = '..src/resources/windows/geckodriver'
                print(self.browser_path)
        else:
            if self.browser_name == 'Chrome':
                self.browser_path = '..src/resources/linux/chromedriver'
                print(self.browser_path)
            else:
                self.browser_path = '..src/resources/linux/geckodriver'
                print(self.browser_path)

a = BaseBuilderLibrary()
a.set_browser("Chrome")
a.set_browser_path()