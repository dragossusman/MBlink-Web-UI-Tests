'''
Created on Nov 10, 2014

@author: dragos.susman
'''
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from lib2to3.tests.support import driver

class HomePageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(1)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def testTopBarElements(self):
        self.driver.get('http://mobilinkgsm.com')
        self.assertTrue(self.driver.find_element_by_class_name('topBar'), 'TopBar is not displayed')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()