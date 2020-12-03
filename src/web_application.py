from src.pages.homepage import HomePage
from src.pages.career_page import CareerPage
from src.pages.header import Header


class WebApplication:

    def __init__(self, driver, env):
        self.driver = driver
        self.homepage = HomePage(driver, env)
        self.career_page = CareerPage(driver, env)
        self.header = Header(driver, env)