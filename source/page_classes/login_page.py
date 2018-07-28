from selenium.webdriver.common.by import By
from source.page_classes.base_page import Base_Page
from source.utilities.selenium_actions import ActionChainsWrapper
import allure

class Login_Page(Base_Page):
    
    #Element declaration
    __helloSignIn = (By.XPATH, "//span[text()='Hello. Sign in']/..")
    __signIn = (By.XPATH, "//span[text()='Sign in']/..")
    __emailTextBox = (By.ID, 'ap_email')
    __continueButton = (By.ID, "continue")
    __passwordTextField = (By.ID, "ap_password")
    __loginButton = (By.ID, "signInSubmit")

    @allure.step("Clicking on the Sign In button")
    def click_on_sign_in(self):
        act = ActionChainsWrapper(self.driver)
        act.moveToElement(self.findElement(*self.__helloSignIn))
        act.click(self.findElement(*self.__signIn))
    
    @allure.step("Entering the contact number and clicking on the continue button")
    def enter_email_or_number(self, contact_number_or_email_address):
        self.sendKeys(*self.__emailTextBox, contact_number_or_email_address)
        self.Click(*self.__continueButton)
        
    @allure.step("Entering the password and clicking on the login button")
    def enter_password(self, password):
        self.sendKeys(*self.__passwordTextField, password)
        self.Click(*self.__loginButton)
        