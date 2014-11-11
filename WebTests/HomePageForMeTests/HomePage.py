'''
Created on Nov 10, 2014

@author: dragos.susman
'''
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from lib2to3.tests.support import driver
from BasePageElement import BasePageElement

class HomePageUITest(BasePageElement):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(1)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def testTopBarElements(self):
        URL = 'http://www.mobilinkgsm.com'
        self.driver.get(URL)
        self.assertTrue(self.findElements('class_name', 'topBar'), 'TopBar is not displayed')
        # For Me
        self.assertEqual(self.findElements('xpath', '//div[@class="topBar"]/div/div/div/ul/li[1]/a').get_attribute('href'), 'http://www.mobilink.com.pk/', 
                         'For Me option in topBar Menu does not have the correct link or is not displayed in home page')
        self.assertEqual(self.findElements('xpath', '//div[@class="topBar"]/div/div/div/ul/li[1]/a').text, 'For Me', 
                         'For Me option text is incorrect')
        
        # For Business
        self.assertEqual(self.findElements('xpath', '//div[@class="topBar"]/div/div/div/ul/li[2]/a').get_attribute('href'), 'http://www.mobilink.com.pk/business', 
                         'For Business option in topBar Menu does not have the correct link or is not displayed in home page')
        self.assertEqual(self.findElements('xpath', '//div[@class="topBar"]/div/div/div/ul/li[2]/a').text, 'For Business', 
                         'For Business option text is incorrect')
        
        # links in topBar
        self.assertTrue(self.findElements('id', 'menu-top-navigation').is_displayed(), 'Links in topBar are not displayed')
        
        # home link
        self.assertTrue(self.findElements('id', 'menu-item-2943').is_displayed(), 'Home link in topBar is not displayed')
        #FIXME: self.assertEqual(self.findElements('xpath', '//*[@id="menu-item-2943"]/a').get_attribute('href'), 'http://www.mobilink.com.pk/', 
        #                 'Home link in topBar Menu does not redirect to correct page')
        self.assertEqual(self.findElements('xpath', '//*[@id="menu-item-2943"]/a').text, 'Home',
                         'Home link does not have the correct text')
        
        # CR - corporate responsibilty
        self.assertTrue(self.findElements('id', 'menu-item-4737').is_displayed(), 'CR link in topBar is not displayed')
        self.assertEqual(self.findElements('xpath', '//*[@id="menu-item-4737"]/a').get_attribute('href'), 'http://www.mobilink.com.pk/about-us/corporate-responsibility/', 
                         'CR link in topBar Menu does not redirect to correct page')
        self.assertEqual(self.findElements('xpath', '//*[@id="menu-item-4737"]/a').text, 'CR',
                         'CR link does not have the correct text')
        
        # Careers
        self.assertTrue(self.findElements('id', 'menu-item-3549').is_displayed(), 'Careers link in topBar is not displayed')
        self.assertEqual(self.findElements('xpath', '//*[@id="menu-item-3549"]/a').get_attribute('href'), 'http://jobs.mobilinkgsm.com/', 
                         'Careers link in topBar Menu does not redirect to correct page')
        self.assertEqual(self.findElements('xpath', '//*[@id="menu-item-3549"]/a').text, 'Careers',
                         'Careers link does not have the correct text')
        
        # About Us
        self.assertTrue(self.findElements('id', 'menu-item-804').is_displayed(), 'About us link in topBar is not displayed')
        self.assertEqual(self.findElements('xpath', '//*[@id="menu-item-804"]/a').get_attribute('href'), 'http://www.mobilink.com.pk/about-us/', 
                         'About us link in topBar Menu does not redirect to correct page')
        self.assertEqual(self.findElements('xpath', '//*[@id="menu-item-804"]/a').text, 'About Us',
                         'About Us link does not have the correct text')
        
        # eCare
        self.assertTrue(self.findElements('id', 'menu-item-4390').is_displayed(), 'eCare link in topBar is not displayed')
        self.assertEqual(self.findElements('xpath', '//*[@id="menu-item-4390"]/a').get_attribute('href'), 'https://ecare.mobilinkgsm.com/', 
                         'eCare link in topBar Menu does not redirect to correct page')
        self.assertEqual(self.findElements('xpath', '//*[@id="menu-item-4390"]/a').text, 'eCare',
                         'eCare link does not have the correct text')
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()