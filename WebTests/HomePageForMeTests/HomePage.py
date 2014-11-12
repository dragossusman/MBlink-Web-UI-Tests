'''
Created on Nov 10, 2014

@author: dragos.susman
'''
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from lib2to3.tests.support import driver
from BasePageElement import BasePageElement
import time

URL = 'http://www.mobilink.com.pk/'

class HomePageUITest(BasePageElement):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def testTopBarElements(self):
        self.openHomePage()
        self.assertTrue(self.findElement('class_name', 'topBar'), 'TopBar is not displayed')
        # For Me
        forMeOption = self.findElement('xpath', '//div[@class="topBar"]/div/div/div/ul/li[1]/a')
        forBusinessOption = self.findElement('xpath', '//div[@class="topBar"]/div/div/div/ul/li[2]/a')
        homeLinkInTopBar = self.findElement('xpath', '//*[@id="menu-item-2943"]/a')
        crLinkInTopBar =  self.findElement('xpath', '//*[@id="menu-item-4737"]/a')
        careersLinkInTopBar = self.findElement('xpath', '//*[@id="menu-item-3549"]/a')
        aboutUsLinkInTopBar = self.findElement('xpath', '//*[@id="menu-item-804"]/a')
        ecareLinkInTopBar = self.findElement('xpath', '//*[@id="menu-item-4390"]/a')
 
        self.getAttributeFromElements('href', forMeOption, URL)
        self.assertEqual(forMeOption.text, 'For Me', 'For Me option text is incorrect')
         
        # For Business
        self.getAttributeFromElements('href', forBusinessOption, URL + 'business')
        self.assertEqual(forBusinessOption.text, 'For Business', 'For Business option text is incorrect')
         
        # links in topBar
        self.assertTrue(self.findElement('id', 'menu-top-navigation').is_displayed(), 'Links in topBar are not displayed')
         
        # home link
        self.assertTrue(self.findElement('id', 'menu-item-2943').is_displayed(), 'Home link in topBar is not displayed')
        self.getAttributeFromElements('href', homeLinkInTopBar, URL)
        self.assertEqual(homeLinkInTopBar.text, 'Home',
                         'Home link does not have the correct text')
         
        # CR - corporate responsibilty
        self.assertTrue(self.findElement('id', 'menu-item-4737').is_displayed(), 'CR link in topBar is not displayed')
        self.getAttributeFromElements('href', crLinkInTopBar, URL + 'about-us/corporate-responsibility/')
        self.assertEqual(crLinkInTopBar.text, 'CR',
                         'CR link does not have the correct text')
         
        # Careers
        self.assertTrue(self.findElement('id', 'menu-item-3549').is_displayed(), 'Careers link in topBar is not displayed')
        self.getAttributeFromElements('href', careersLinkInTopBar, 'http://jobs.mobilinkgsm.com/')
        self.assertEqual(careersLinkInTopBar.text, 'Careers',
                         'Careers link does not have the correct text')
         
        # About Us
        self.assertTrue(self.findElement('id', 'menu-item-804').is_displayed(), 'About us link in topBar is not displayed')
        self.getAttributeFromElements('href', aboutUsLinkInTopBar, URL + 'about-us/')
        self.assertEqual(aboutUsLinkInTopBar.text, 'About Us',
                         'About Us link does not have the correct text')
         
        # eCare
        self.assertTrue(self.findElement('id', 'menu-item-4390').is_displayed(), 'eCare link in topBar is not displayed')
        self.getAttributeFromElements('href', ecareLinkInTopBar, 'https://ecare.mobilinkgsm.com/')
        self.assertEqual(ecareLinkInTopBar.text, 'eCare',
                         'eCare link does not have the correct text')
         
    def testLogo(self):
        self.openHomePage()
        self.getAttributeFromElements('class', self.findElement('xpath', '//div[@class="mobilink_website"]/div[2]/div[1]/div/div[1]/h2'), 'logo')
        self.assertEqual(self.findElement('xpath', '//div[@class="mobilink_website"]/div[2]/div[1]/div/div[1]/h2/a').text, 'Mobilink', 
                         'The text in logo on homepage is not correct')
         
    def testSocialLinks(self):
        self.openHomePage()
        # Facebook
        self.getAttributeFromElements('href', self.findElement('xpath', '//div[@class="mobilink_website"]/div[2]/div[1]/div/div[2]/ul/li[2]/a'), 'http://www.facebook.com/Mobilink')
        self.getAttributeFromElements('class', self.findElement('xpath', '//div[@class="mobilink_website"]/div[2]/div[1]/div/div[2]/ul/li[2]/a'), 'icon_facebook')
        # Linkedin
        self.getAttributeFromElements('href', self.findElement('xpath', '//div[@class="mobilink_website"]/div[2]/div[1]/div/div[2]/ul/li[3]/a'), 'https://twitter.com/Mobilink')
        self.getAttributeFromElements('class', self.findElement('xpath', '//div[@class="mobilink_website"]/div[2]/div[1]/div/div[2]/ul/li[3]/a'), 'icon_twitter')
         
    def testMainMenuElements(self):
        self.openHomePage()
        self.assertTrue(self.findElement('id', 'megaMenu').is_displayed(), 'Main menu is not displayed on home page')
        # Prepaid option
        self.assertTrue(self.findElement('xpath', '//*[@id="menu-item-82"]/a').get_attribute('href').find('prepaid'), 
                        'Prepaid option in main menu does not redirect to correct link')
        self.assertEqual(self.findElement('xpath', '//*[@id="menu-item-82"]/a/span').text, 'Prepaid',
                        'Prepaid option in main menu has incorrect text')
        # Postpaid option
        self.assertTrue(self.findElement('xpath', '//*[@id="menu-item-178"]/a').get_attribute('href').find('postpaid'), 
                        'Postpaid option in main menu does not redirect to correct link')
        self.assertEqual(self.findElement('xpath', '//*[@id="menu-item-178"]/a/span').text, 'Postpaid',
                        'Postpaid option in main menu has incorrect text')
        # Mobile Internet
        self.assertTrue(self.findElement('xpath', '//*[@id="menu-item-4334"]/a').get_attribute('href').find('mobile-internet'), 
                        'Mobile Internet option in main menu does not redirect to correct link')
        self.assertEqual(self.findElement('xpath', '//*[@id="menu-item-4334"]/a/span').text, 'Mobile Internet',
                        'Mobile Internet option in main menu has incorrect text')
        # Intl Roaming
        self.assertTrue(self.findElement('xpath', '//*[@id="menu-item-9010"]/a').get_attribute('href').find('ir'), 
                        'Intl Roaming option in main menu does not redirect to correct link')
        # Value Added Services
        self.assertTrue(self.findElement('xpath', '//*[@id="menu-item-408"]/a').get_attribute('href').find('vas'), 
                        'Value Added Services option in main menu does not redirect to correct link')
        self.assertEqual(self.findElement('xpath', '//*[@id="menu-item-408"]/a/span').text, 'Value Added Services',
                        'Value Added Services option in main menu has incorrect text')
        # Customer Care
        self.assertTrue(self.findElement('xpath', '//*[@id="menu-item-185"]/a').get_attribute('href').find('customer-care'), 
                        'Customer Care option in main menu does not redirect to correct link')
        self.assertEqual(self.findElement('xpath', '//*[@id="menu-item-185"]/a/span').text, 'Customer Care',
                        'Customer Care option in main menu has incorrect text')
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()