from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class CareerPage:
    OUR_LOCATIONS = (By.ID, "career-our-location")
    TEAMS_SECTION = (By.ID, "career-find-our-calling")
    LIFE_AT_INSIDER = (By.XPATH, "//h2[contains(@class, 'elementor-heading-title') and contains(text(), 'Life at Insider')]")
    ACCEPT_COOKIES_BTN = (By.ID, "wt-cli-accept-all-btn")
    SEE_ALL_QA_JOBS_BTN = (By.XPATH, '//*[@id="page-head"]/div/div/div[1]/div/div/a')
    LOCATION_DROPDOWN = (By.XPATH, '//*[@id="top-filter-form"]/div[1]/span/span[1]/span')
    LOCATION_OPTION_TEMPLATE = "//li[contains(text(), '{}')]"
    DEPARTMENT_DROPDOWN = (By.XPATH, '//*[@id="top-filter-form"]/div[2]/span/span[1]/span')
    DEPARTMENT_OPTION_TEMPLATE = "//li[contains(text(), '{}')]"
    JOBS_LIST = (By.ID, "jobs-list")
    FIRST_JOB_ELEMENT = (By.XPATH, '//*[@id="jobs-list"]/div[1]/div')
    FIRST_VIEW_ROLE_BUTTON = (By.XPATH, '//*[@id="jobs-list"]/div[1]/div/a')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Checks the visibility of the 'Our Locations' section.
    def is_our_locations_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.OUR_LOCATIONS))
        return True

    # Checks the visibility of the 'Teams' section.
    def is_teams_section_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.TEAMS_SECTION))
        return True

    # Checks the visibility of the 'Life at Insider' title.
    def is_life_at_insider_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.LIFE_AT_INSIDER))
        return True

    # Goes to the Quality Assurance career page.
    def go_to_quality_assurance_page(self):
        self.driver.get("https://useinsider.com/careers/quality-assurance/")

    # Accepts the cookie popup.
    def accept_cookies_popup(self):
        try:
            accept_btn = self.wait.until(EC.element_to_be_clickable(self.ACCEPT_COOKIES_BTN))
            accept_btn.click()
            print("✅ Cookies accepted.")
        except:
            print("⚠ Cookies popup not found or already accepted.")

    # He/She clicks the button to handle all QA tasks.
    def click_see_all_qa_jobs(self):
        see_all_btn = self.wait.until(EC.element_to_be_clickable(self.SEE_ALL_QA_JOBS_BTN))
        see_all_btn.click()

    # Opens the location filter and selects the chosen location.
    def filter_by_location(self, location_name="Istanbul, Turkey"):
        self.wait.until(EC.element_to_be_clickable(self.LOCATION_DROPDOWN)).click()
        option_locator = (By.XPATH, self.LOCATION_OPTION_TEMPLATE.format(location_name))
        self.wait.until(EC.element_to_be_clickable(option_locator)).click()

    # Opens the department filter and selects the chosen department.
    def filter_by_department(self, department_name="Quality Assurance"):
        self.wait.until(EC.element_to_be_clickable(self.DEPARTMENT_DROPDOWN)).click()
        option_locator = (By.XPATH, self.DEPARTMENT_OPTION_TEMPLATE.format(department_name))
        self.wait.until(EC.element_to_be_clickable(option_locator)).click()

    # It applies both the location and department filters.
    def filter_jobs(self, location="Istanbul, Turkey", department="Quality Assurance"):
        self.filter_by_location(location)
        self.filter_by_department(department)

    # hovers over the job listing and clicks the 'View Role' button.
    def hover_and_click_first_view_role(self):
        self.wait.until(EC.presence_of_element_located(self.JOBS_LIST))
        job_element = self.wait.until(EC.presence_of_element_located(self.FIRST_JOB_ELEMENT))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", job_element)
        actions = ActionChains(self.driver)
        actions.move_to_element(job_element).perform()
        view_role_button = self.wait.until(EC.element_to_be_clickable(self.FIRST_VIEW_ROLE_BUTTON))
        actions.move_to_element(view_role_button).click().perform()



