from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebElementWait:

    def __init__(self, browser, timetowait=5):
        self.browser = browser
        self.timetowait = timetowait

    def wait_till_present(self, by_type, locator):
        return WebDriverWait(self.browser, self.timetowait).until(
            EC.presence_of_element_located((by_type, locator)))

    def wait_till_visible(self, by_type, locator):
        return WebDriverWait(self.browser, self.timetowait).until(
            EC.visibility_of_element_located((by_type, locator)))

    def wait_till_invisible(self, by_type, locator):
        return WebDriverWait(self.browser, self.timetowait).until(
            EC.invisibility_of_element_located((by_type, locator)))

    def wait_till_clickable(self, by_type, locator):
        return WebDriverWait(self.browser, self.timetowait).until(
            EC.element_to_be_clickable((by_type, locator)))

    def wait_till_not_present(self, by_type, locator):
        return WebDriverWait(self.browser, self.timetowait).until(
            EC.staleness_of((by_type, locator)))

    def wait_till_elements_visible(self, by_type, locator):
        return WebDriverWait(self.browser, self.timetowait).until(
            EC.visibility_of_all_elements_located((by_type, locator)))

