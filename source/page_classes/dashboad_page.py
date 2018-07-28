from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from source.page_classes.base_page import Base_Page


class Dashboard_Page(Base_Page):
    
        __search_box = (By.ID, "twotabsearchtextbox")
        __mobile = (By.XPATH, "//h2[text()='Apple iPhone X (Space Grey, 64GB)']/..")
        __add_to_cart = (By.ID, "add-to-cart-button")
        __successMessage = (By.XPATH, "//div[@id='huc-v2-order-row-confirm-text']")
                
        def enter_the_product(self, product_name):
            self.sendKeys(*self.__search_box, product_name)
            self.sendKeys(*self.__search_box, Keys.ENTER) 
            
        def click_on_mobile(self):
            self.Click(*self.__mobile) 
        
        def click_on_add_to_cart(self): 
            self.Click(*self.__add_to_cart)
            
        def get_success_message(self):
            success_message = self.findElement(*self.__successMessage)
            return success_message.text
    
    