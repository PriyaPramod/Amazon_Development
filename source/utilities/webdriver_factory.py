from selenium import webdriver
import constants
from source.utilities import excel_automation as excel

def get_driver():
    browserName = excel.get_cell_value(constants.EXCEL_FILE_PATH, 'Settings', 0, 'BrowserName')
    URL = excel.get_cell_value(constants.EXCEL_FILE_PATH, 'Settings', 0, 'URL')
    
    if browserName == 'Chrome':
        driver = webdriver.Chrome(constants.CHROME_VALUE)
    else:
        driver = webdriver.Firefox()
    
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(URL)
    
    return driver