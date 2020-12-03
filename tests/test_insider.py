import pytest
import allure
import time


@allure.feature('Insider Tests')
@allure.suite('Homepage Tests')
@pytest.mark.ui
class TestHomepage:

    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_homepage_opens(self, webapp):
        allure.dynamic.title("Visit https://useinsider.com/ and check Insider home page is opened")
        webapp.homepage.open_page(webapp.homepage.url)
        webapp.homepage.verify_hp_opened()

@allure.feature('Insider Tests')
@allure.suite('Career Tests')
@pytest.mark.ui
class TestCareer:

    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_career_jobs_opens(self, webapp):
        allure.dynamic.title("Select Career menu in navigation bar and check Career page Jobs block is opened")
        webapp.homepage.open_page(webapp.homepage.url)
        webapp.header.navigate_to_career()
        webapp.career_page.verify_jobs_opened()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_jobs_search_works(self, webapp):
        allure.dynamic.title("Scroll to Career Opportunities, filter jobs by Location - Istanbul, Turkey and "
                             "department - Quality Assurance, check presence of jobs list")
        webapp.career_page.open_page(webapp.career_page.url)
        webapp.career_page.scroll_to_search()
        webapp.career_page.perform_search()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_jobs_search_returns_correct_results(self, webapp):
        allure.dynamic.title("Verify the search is correct")
        webapp.career_page.open_page(webapp.career_page.url)
        webapp.career_page.scroll_to_search()
        webapp.career_page.perform_search()
        time.sleep(5)
        webapp.career_page.verify_search_results()
