from selenium.webdriver.common.action_chains import ActionChains
import allure

class ActionChainsWrapper:
    
    def __init__(self, driver):
        self.action = ActionChains(driver)

    @allure.step("Moving the mouse pointer on the element")
    def moveToElement(self, element):
        try:
            self.action.move_to_element(element).pause(2)
            self.action.perform()
        except:
            print('Not able to perform mouse hover action')
     
    @allure.step("Clicking on the drop down element")   
    def click(self, element):
        try:
            self.action.click(element).pause(2)
            self.action.perform()
        except:
            print('Not able to click on the element')
    