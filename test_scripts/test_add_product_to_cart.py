from source.page_classes.PageManager import get_login_page, get_dashboard_page
from source.utilities import excel_automation as excel
import constants
import allure
import pytest


class Test_product():
    
    #@pytest.allure.description("Adding the product and verifying in cart")
    def test_add_product_to_cart(self, request):
        contact_number = excel.get_cell_value(constants.EXCEL_FILE_PATH, 'Login', 0, 'Username')
        password = excel.get_cell_value(constants.EXCEL_FILE_PATH, 'Login', 0, 'Password')
        '''product_name = excel.get_cell_value(constants.EXCEL_FILE_PATH, 'Login', 0, 'ProductName')
        message = excel.get_cell_value(constants.EXCEL_FILE_PATH, 'Login', 0, 'successMessage')'''
        
        login = get_login_page(request.node.driver)
        login.click_on_sign_in()
        login.enter_email_or_number(contact_number)
        login.enter_password(password)
        
        assert False


    #@pytest.allure.description("Adding the product and verifying in cart")
    def test_add_product_to_cart_one(self, request):
        contact_number = excel.get_cell_value(constants.EXCEL_FILE_PATH, 'Login', 0, 'Username')
        password = excel.get_cell_value(constants.EXCEL_FILE_PATH, 'Login', 0, 'Password')
        
        login = get_login_page(request.node.driver)
        login.click_on_sign_in()
        login.enter_email_or_number(contact_number)
        login.enter_password(password)
    
    #@pytest.allure.description("Adding the product and verifying in cart")    
    def test_add_product_to_cart_two(self, request):
        contact_number = excel.get_cell_value(constants.EXCEL_FILE_PATH, 'Login', 0, 'Username')
        password = excel.get_cell_value(constants.EXCEL_FILE_PATH, 'Login', 0, 'Password')
        
        login = get_login_page(request.node.driver)
        login.click_on_sign_in()
        login.enter_email_or_number(contact_number)
        login.enter_password(password)
        
        assert False