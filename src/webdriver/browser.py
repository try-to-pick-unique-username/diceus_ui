import allure
from selenium import webdriver

from src.tools.logger import logger, log_exception

class Browser:

    def __init__(self, browser_name):
        self.open(browser_name)

    @allure.step('Starting the {browser_name}')
    def open(self, browser_name):
        logger.info(f'Starting the {browser_name}')
        if browser_name == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser_name == 'chrome':
            self.driver = webdriver.Chrome()
        else:
            raise ValueError(
                log_exception(f'The {browser_name} is not supported yet'))
        self.driver.maximize_window()

    @allure.step('Closing the browser')
    def close(self):
        logger.info('Closing the browser')
        self.driver.quit()

    @allure.step('Saving the screenshot')
    def save_scr(self):
        logger.info('Saving the screenshot')
        self.driver.get_screenshot_as_png()

