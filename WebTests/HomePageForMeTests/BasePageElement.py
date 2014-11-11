'''
Created on Nov 11, 2014

@author: dragos.susman
'''
import unittest
import this


class BasePageElement(unittest.TestCase):
    
    # method used to find elements in page based on identifiers
    def findElements(self, param, locator):
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
        titles = { self.findElements('xpath', '//div[@class="topBar"]/div/div/div/ul/li[1]/a') : 'For Me' }
        self.assertEqual(element.text, titles[element], element + 'has the correct text')    
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()