import allure

from src.pages.base_page import BasePage
from src.tools.logger import logger, log_exception
from src.pages.locators.insider_locators import *

class Header(BasePage):


    @allure.step('Navigating to the Career page')
    def navigate_to_career(self):
        logger.info('Navigating to the Career page')
        self.click(*CAREER_MENU_LINK)

