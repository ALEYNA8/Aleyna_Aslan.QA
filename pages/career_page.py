from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class CareerPage:
    def __init__(self, driver):
        # We are creating the WebDriverWait object.
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # 'Is the 'Our Locations' visible check
    def is_our_locations_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "career-our-location")))
            return True
        except:
            return False

    # Check if the 'Teams' section is visible.
    def is_teams_section_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "career-find-our-calling")))
            return True
        except:
            return False

    # Check if the title 'Life at Insider' is visible
    def is_life_at_insider_visible(self):
        locator = (By.XPATH, "//h2[contains(@class, 'elementor-heading-title') and contains(text(), 'Life at Insider')]")
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    # Go to the Quality Assurance page
    def go_to_quality_assurance_page(self):
        self.driver.get("https://useinsider.com/careers/quality-assurance/")

    # Accept the cookie consent popup
    def accept_cookies_popup(self):
        try:
            accept_btn = self.wait.until(
                EC.element_to_be_clickable((By.ID, "wt-cli-accept-all-btn"))
            )
            accept_btn.click()
            print("✅ Cookies accepted.")
        except:
            print("⚠ Cookies popup not found or already accepted.")

    # Click on the 'See all QA jobs' button
    def click_see_all_qa_jobs(self):
        see_all_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="page-head"]/div/div/div[1]/div/div/a'))
        )
        see_all_btn.click()

    # Open the location filter and select
    def filter_by_location(self, location_name="Istanbul, Turkey"):
        location_dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="top-filter-form"]/div[1]/span/span[1]/span'))
        )
        location_dropdown.click()
        option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{location_name}')]"))
        )
        option.click()

    # Open the department filter and select
    def filter_by_department(self, department_name="Quality Assurance"):
        department_dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="top-filter-form"]/div[2]/span/span[1]/span'))
        )
        department_dropdown.click()
        option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{department_name}')]"))
        )
        option.click()

    # Apply both location and department filters
    def filter_jobs(self, location="Istanbul, Turkey", department="Quality Assurance"):
        self.filter_by_location(location)
        self.filter_by_department(department)

    # Hover over the first job listing and click the 'View Role' button.
    def hover_and_click_first_view_role(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "jobs-list")))

        job_element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="jobs-list"]/div[1]/div'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", job_element)

        actions = ActionChains(self.driver)
        actions.move_to_element(job_element).perform()

        view_role_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="jobs-list"]/div[1]/div/a'))
        )
        actions.move_to_element(view_role_button).click().perform()


