from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

class MyListeners(AbstractEventListener):
    
    def before_navigate_to(self, url, driver):
        print("before_navigate_to")

    def after_navigate_to(self, url, driver):
        print("after_navigate_to")

    def before_navigate_back(self, driver):
        print("before_navigate_back")

    def after_navigate_back(self, driver):
        print("after_navigate_back")

    def before_navigate_forward(self, driver):
        print("before_navigate_forward")

    def after_navigate_forward(self, driver):
        print("after_navigate_forward")

    def before_find(self, by, value, driver):
        print("before_find")

    def after_find(self, by, value, driver):
        print("after_find")

    def before_click(self, element, driver):
        print("before_click")

    def after_click(self, element, driver):
        print("after_click")

    def before_change_value_of(self, element, driver):
        print("before_change_value_of")

    def after_change_value_of(self, element, driver):
        print("before_change_value_of")

    def before_execute_script(self, script, driver):
        print("before_execute_script")

    def after_execute_script(self, script, driver):
        print("after_execute_script")

    def before_close(self, driver):
        print("before_close")

    def after_close(self, driver):
        print("after_close")

    def before_quit(self, driver):
        pass

    def after_quit(self, driver):
        pass

    def on_exception(self, exception, driver):
        pass

    
    