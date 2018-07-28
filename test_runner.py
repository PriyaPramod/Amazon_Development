import os
import pytest
from datetime import datetime


class My_plugin():
    
    def pytest_sessionfinish(self):
        allure_report_folder = 'reports/html_reports/Test_Reports_' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        os.popen('allure generate ./reports/allure-result/ -o ./' + allure_report_folder)


arguments = ['-v', '--alluredir', './reports/allure-result']
pytest.main(args=arguments, plugins=[My_plugin()])
