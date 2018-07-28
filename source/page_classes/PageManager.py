from source.page_classes.dashboad_page import Dashboard_Page
from source.page_classes.login_page import Login_Page

def get_login_page(driver):
    login  = Login_Page(driver)
    return login

def get_dashboard_page(driver):
    dashboard = Dashboard_Page(driver)
    return dashboard