import os
import pytest
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
import constants
from source.utilities import webdriver_factory as wdf
from source.utilities.listeners import MyListeners
import allure

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(scope="session", autouse=True)
def set_environment():
    os.environ[constants.CHROME_KEY] = constants.CHROME_VALUE
    os.environ[constants.FIREFOX_KEY] = constants.FIREFOX_VALUE

@pytest.fixture(scope="function", autouse=True)
def setUp(request):
    
    W_driver = wdf.get_driver()
    driver = EventFiringWebDriver(W_driver, MyListeners())
    if request.node is not None:
        request.node.driver = driver
    yield
    if request.node.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name=request.function.__name__, attachment_type=allure.attachment_type.PNG)
    driver.quit()