import allure

from src.pages.base_page import BasePage
from src.tools.logger import logger, log_exception
from src.test_data.validation_data import HOMEPAGE_TITLE


class HomePage(BasePage):

    @property
    def url(self):
        return self.env.get('host', None)

    @allure.step('Verifying that the homepage is opened')
    def verify_hp_opened(self):
        logger.info('Verifying that the homepage is opened')
        assert self.get_title() == HOMEPAGE_TITLE, log_exception('The homepage was not opened')

