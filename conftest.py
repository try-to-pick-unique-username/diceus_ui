import pytest
import allure

from src.tools.logger import logger, log_exception
from src.tools.config_reader import ConfigurationReader
from src.webdriver.browser import Browser
from src.web_application import WebApplication


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--env", default="qa")

@pytest.fixture(autouse=True)
def pretty_test_info(request):
    logger.info('*' * 10 + f'START TEST {str(request.node.name)}' + '*' * 10)
    yield
    logger.info('*' * 10 + f'END TEST {str(request.node.name)}' + '*' * 10)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    marker = item.get_closest_marker("ui")
    if marker:
        if rep.when == "call" and rep.failed:
            try:
                driver = item.funcargs['webapp'].driver
                allure.attach(driver.save_scr(),
                              name=item.name,
                              attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(e)

@pytest.fixture(scope="session")
def env(request):
    environment = request.config.getoption("--env")
    config = ConfigurationReader()
    return config.read(environment)

@pytest.fixture(scope='session')
def driver(request):
    browser_name = request.config.getoption('browser')
    browser = Browser(browser_name)
    yield browser
    browser.close()

@pytest.fixture()
def webapp(driver, env):
    webapp = WebApplication(driver, env)
    return webapp
