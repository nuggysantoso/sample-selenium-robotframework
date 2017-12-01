import sys
import os

class BaseBuilder(object):
    platform_Name = None
    browser_Name = None
    browser_Path = None

    def get_Platform(self):
        self.platform_Name = sys.platform
        return self.platform_Name

    def set_Browser(self, browser_Name):
        self.browser_Name = browser_Name

    def set_Browser_Path(self):
        self.get_Platform()
        if self.platform_Name =='darwin':
            if self.browser_Name == 'Chrome':
                self.browser_Path = '..src/resources/mac/chromedriver'
                print(self.browser_Path)
            else:
                self.browser_Path = '..src/resources/mac/geckodriver'
                print(self.browser_Path)
        elif self.platform_Name == 'win32':
            if self.browser_Name == 'Chrome':
                self.browser_Path = '..src/resources/windows/chromedriver'
                print(self.browser_Path)
            else:
                self.browser_Path = '..src/resources/windows/geckodriver'
                print(self.browser_Path)
        else:
            if self.browser_Name == 'Chrome':
                self.browser_Path = '..src/resources/linux/chromedriver'
                print(self.browser_Path)
            else:
                self.browser_Path = '..src/resources/linux/geckodriver'
                print(self.browser_Path)

a = BaseBuilder()
a.set_Browser('Firefox')
a.set_Browser_Path()