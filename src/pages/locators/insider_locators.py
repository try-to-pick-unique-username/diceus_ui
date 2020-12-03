from selenium.webdriver.common.by import By


GO_BUTTON = (By.LINK_TEXT, "GO")
CAREER_MENU_LINK = (By.XPATH, "//li[@id='menu-item-21643']/a")
CAREER_CULTURE_LINK = (By.XPATH, "//a[@href='#culture']")
CAREER_LOCATIONS_LINK = (By.XPATH, "//a[@href='#locations']")
CAREER_TEAMS_LINK = (By.XPATH, "//a[@href='#teams']")
CAREER_JOBS_LINK = (By.XPATH, "//a[@href='#jobs']")
CAREER_LIFE_LINK = (By.XPATH, "//a[@href='#life-at-insider']")
CAREER_JOBS_HEADING = (By.XPATH, "//div[@id='jobs']/div[2]/div/div/div/h2")
CAREER_JOBS_PARAGRAPH = (By.XPATH, "//div[@id='jobs']/div[2]/div/div/div/div/div/p")
CAREER_JOBS_LOCATION_FILTER_ISTANBUL = (By.XPATH, "//option[@class='job-location Istanbul,Turkey']")
CAREER_JOBS_DEPARTMENT_FILTER_QA = (By.XPATH, "//option[@class='job-team QualityAssurance']")
CAREER_JOBS_RESULTS_LIST = (By.XPATH, "//div[@class='jobs-list']")
CAREER_JOBS_RESULT_ITEM = (By.XPATH, "//div[@class='jobs-list']/a")

