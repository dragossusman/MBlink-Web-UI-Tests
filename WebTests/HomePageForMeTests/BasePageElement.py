'''
Created on Nov 11, 2014

@author: dragos.susman
'''
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import os, json

class BasePageElement(unittest.TestCase):
    
    # method used to find elements in page based on identifiers
    def findElement(self, param, locator):
        if param == 'class_name':
            return self.Driver.find_element_by_class_name(locator)
        if param == 'id':
            return self.Driver.find_element_by_id(locator)
        if param == 'name':
            return self.Driver.find_element_by_name(locator)
        if param == 'xpath':
            return self.Driver.find_element_by_xpath(locator)
    
    # method used to get the text from all web elements in page
    def getTextFromElements(self, element):
        # checks an element's text
        titles = { self.findElement('xpath', '//div[@class="topBar"]/div/div/div/ul/li[1]/a') : 'ForMe' }
        self.assertEqual(element.text, titles[element], 'The' + element + 'has incorrect text')
        
    # open main page URL
    def openHomePage(self):
        #URL = 'http://www.mobilinkgsm.com'
        self.Driver.get(self.Config['URL'])
        
    def getAttributeFromElements(self, attribute, element, string):
        if attribute == 'href':  
            self.assertEqual(element.get_attribute(attribute), string, 'The element tested does not redirect to correct link') 
        elif attribute == 'class':
            self.assertEqual(element.get_attribute(attribute), string, 'The element tested does not have the expected class attribute')
        elif attribute == 'style':
            self.assertEqual(element.get_attribute(attribute), string, 'The element tested does not have the expected style attribute')
    def openSubMenuDropDown(self, element):
        browser = self.Config['Browser']
        # move to element function doesn't work well; the only solution was this rudimentary one
        if browser == 'Chrome':
            ActionChains(self.Driver).move_to_element(element).perform()
        elif browser == 'Firefox':
            ActionChains(self.Driver).move_to_element(element).perform()
            ActionChains(self.Driver).move_to_element(element).perform()
        # unless we set a sleep time the test fails
        time.sleep(5)
    
    @staticmethod
    def Configure(self):
        jsonPath = os.getenv("CONFIG_JSON");
        print ("CONFIG_JSON:" + jsonPath)
        if (os.path.isfile(jsonPath)):
            config = json.loads(open(jsonPath, 'r').read())
        else:
            raise NameError("Cannot find config json as a system variable")
        currentDir = os.path.dirname(os.path.realpath(__file__))

        self.Config = config
        browser = self.Config['Browser']
        args = None
        if browser == 'Chrome':
            chromedriver = self.Config['FilesDir'] + "\\chromedriver"
            os.environ["webdriver.chrome.driver"] = str(chromedriver)
            args = [chromedriver]
        
        driver = getattr(webdriver, browser)
        if args is None:
            self.Driver = driver()
        else:
            self.Driver = driver(*args)
        self.browser = browser
        self.Driver.maximize_window()
        self.windows = [ self.Driver ]
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()