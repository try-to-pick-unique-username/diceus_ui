import allure

from src.webdriver.web_element_wait import WebElementWait
from src.tools.logger import logger, log_exception


class BasePage(object):
    def __init__(self, browser, env):
        self.browser = browser.driver
        self.env = env
        self.element_wait = WebElementWait(self.browser)

    @allure.step('Navigating to {url}')
    def open_page(self, url):
        logger.info(f'Navigating to {url}')
        self.browser.get(url)

    @allure.step('Getting the page title')
    def get_title(self):
        logger.info('Getting the page title')
        return self.browser.title

    @allure.step('Reloading the page')
    def reload_page(self):
        logger.info('Reloading the page')
        self.browser.get(self.browser.current_url)

    def scroll_to_element(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def find(self, selector_type, selector):
        return self.element_wait.wait_till_present(selector_type, selector)

    def click(self, selector_type, selector):
        self.element_wait.wait_till_clickable(selector_type, selector).click()

    def get_attribute_value(self, element, attribute):
        return element.get_attribute(attribute)

    def get_text(self, selector_type, selector):
        return self.find(selector_type, selector).text

    def find_many(self, selector_type, selector):
        return self.element_wait.wait_till_elements_visible(selector_type, selector)
