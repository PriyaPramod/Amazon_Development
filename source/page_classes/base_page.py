from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import constants

class Base_Page():
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.set_page_load_timeout(constants.PAGE_TIME_OUT)
        
    def findElement(self, by_type, value):
        try:
            return self.driver.find_element(by_type, value)
        except NoSuchElementException:
            print('Element not found')
    
    def Click(self, by_type, value):
        try:
            element = self.findElement(by_type, value)
            element.click()
        except Exception:
            print(Exception)
            print('Not able to click on the element')
            
    def sendKeys(self, by_type, value, text_to_enter):
        try:
            element = self.findElement(by_type, value)
            element.send_keys(text_to_enter)
        except Exception:
            print(Exception)
            print('Not able to enter the text into the element')
      
    def verifyPageIsDisplayed(self, title_of_the_page):
        wait = self.webDriverWait()
        try:
            wait.until(ec.title_contains(title_of_the_page)) 
            print("Pass: Expected page is displayed")
        except TimeoutException:
            print("Fail: Expected page is not displayed") 
            assert False        
    
    def webDriverWait(self):
        return WebDriverWait(self.driver, constants.EXPECTED_TIME_OUT)
    
    def verifyTheText(self, element, expected_text):
        actual_text = element.text
        assert actual_text == expected_text