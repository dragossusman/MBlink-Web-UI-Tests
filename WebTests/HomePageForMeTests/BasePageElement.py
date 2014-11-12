'''
Created on Nov 11, 2014

@author: dragos.susman
'''
import unittest
import this
from lib2to3.tests.support import driver


class BasePageElement(unittest.TestCase):
    
    # method used to find elements in page based on identifiers
    def findElement(self, param, locator):
        if param == 'class_name':
            return self.driver.find_element_by_class_name(locator)
        if param == 'id':
            return self.driver.find_element_by_id(locator)
        if param == 'name':
            return self.driver.find_element_by_name(locator)
        if param == 'xpath':
            return self.driver.find_element_by_xpath(locator)
    
    # method used to get the text from all web elements in page
    def getTextFromElements(self, element):
        # checks an element's text
        titles = { self.findElement('xpath', '//div[@class="topBar"]/div/div/div/ul/li[1]/a') : 'ForMe' }
        self.assertEqual(element.text, titles[element], 'The' + element + 'has incorrect text')
        
    # open main page URL
    def openHomePage(self):
        URL = 'http://www.mobilinkgsm.com'
        self.driver.get(URL)
        
    def getAttributeFromElements(self, attribute, element, string):
        if attribute == 'href':  
            self.assertEqual(element.get_attribute(attribute), string, 'The element tested does not redirect to correct link') 
        elif attribute == 'class':
            self.assertEqual(element.get_attribute(attribute), string, 'The element tested does not have the expected class attribute') 
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()