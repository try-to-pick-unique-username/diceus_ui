import allure

from src.pages.base_page import BasePage
from src.tools.logger import logger, log_exception
from src.pages.locators.insider_locators import *
from src.test_data.validation_data import *


class CareerPage(BasePage):

    @property
    def url(self):
        return self.env.get('host', None) + '/career'

    @allure.step('Verifying that the jobs section is opened')
    def verify_jobs_opened(self):
        logger.info('Verifying that the jobs section is opened')
        self.click(*CAREER_JOBS_LINK)
        assert self.get_text(*CAREER_JOBS_HEADING) == CAREER_JOBS_HEADING_TEXT, log_exception('The heading text is absent/wrong')
        assert self.get_text(*CAREER_JOBS_PARAGRAPH) == CAREER_JOBS_PARAGRAPH_TEXT, log_exception('The paragraph text is absent/wrong')

    @allure.step('Scrolling to the jobs search')
    def scroll_to_search(self):
        logger.info('Scrolling to the jobs search')
        self.scroll_to_element(self.find(*CAREER_JOBS_LINK))

    @allure.step('Performing the search with filters: Istanbul + QA')
    def perform_search(self):
        logger.info('Performing the search with filters: Istanbul + QA')
        self.click(*CAREER_JOBS_LOCATION_FILTER_ISTANBUL)
        self.click(*CAREER_JOBS_DEPARTMENT_FILTER_QA)
        self.find(*CAREER_JOBS_RESULTS_LIST)


    @allure.step('Verifying the search results')
    def verify_search_results(self):
        logger.info('Verifying the search results')
        results = self.find_many(*CAREER_JOBS_RESULT_ITEM)
        for item in results:
            actual_values = (self.get_attribute_value(item, 'data-location'), self.get_attribute_value(item, 'data-team'))
            assert actual_values == CAREER_JOBS_RESULT_ITEM_VALUES, log_exception('The search results are incorrect')


