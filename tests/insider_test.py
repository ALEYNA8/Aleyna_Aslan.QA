import time
import os

from selenium.common import TimeoutException
from tests.base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.career_page import CareerPage

class InsiderTest(BaseTest):

    # Screenshot function
    def _take_screenshot(self, name_prefix):
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        file_path = os.path.join(screenshot_dir, f"{name_prefix}_{timestamp}.png")
        self.driver.save_screenshot(file_path)
        print(f"Screenshot saved to {file_path}")

    # Homepage and career page tests
    def test_home_page_and_careers_page(self):
        self.driver.get("https://useinsider.com/")
        home_page = HomePage(self.driver)
        assert home_page.is_on_home_page(), "The current URL is not the home page!"
        time.sleep(3)

        # Accept cookies
        try:
            accept_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, "wt-cli-accept-all-btn"))
            )
            accept_btn.click()
            print("✅ Cookies accepted.")
        except:
            print("Cookies accept button not found or already accepted.")
        time.sleep(2)

        # Go to the career page
        home_page.click_careers()
        WebDriverWait(self.driver, 10).until(EC.url_contains("careers"))
        self.assertIn("careers", self.driver.current_url, "Not on Careers page!")

        career_page = CareerPage(self.driver)

        # Check the visibility of the blocks on the career page.
        self.assertTrue(career_page.is_our_locations_visible(), "'Our Locations' section not visible!")
        self.assertTrue(career_page.is_teams_section_visible(), "'Teams' section not visible!")
        self.assertTrue(career_page.is_life_at_insider_visible(), "'Life at Insider' section not visible!")

    # Quality Assurance page and job listing viewing test
    def test_quality_assurance_page_and_see_all_jobs(self):
        career_page = CareerPage(self.driver)
        career_page.go_to_quality_assurance_page()
        time.sleep(3)
        career_page.accept_cookies_popup()
        career_page.click_see_all_qa_jobs()
        WebDriverWait(self.driver, 10).until(EC.url_contains("open-positions"))
        self.assertIn("open-positions", self.driver.current_url)
        time.sleep(3)

    # Check the redirection to the new page by clicking the 'View Role' button in the job advertisement.
    def test_click_view_role_and_check_redirect(self):
        career_page = CareerPage(self.driver)

        # If we are not on the correct page, let’s go to the necessary page first.
        if "open-positions" not in self.driver.current_url:
            career_page.go_to_quality_assurance_page()
            career_page.accept_cookies_popup()
            career_page.click_see_all_qa_jobs()
            try:
                WebDriverWait(self.driver, 15).until(EC.url_contains("open-positions"))
            except TimeoutException:
                self.fail("The open positions page did not open on time.")

        time.sleep(3)

        current_windows = self.driver.window_handles

        # Hover over the 'View Role' button and click.
        try:
            career_page.hover_and_click_first_view_role()
        except TimeoutException:
            self._take_screenshot("view_role_button_not_clickable")
            self.fail("The View Role button was not found or could not be clicked.")

        # Wait for the new tab to open and switch to it.
        try:
            WebDriverWait(self.driver, 20).until(lambda d: len(d.window_handles) > len(current_windows))
            new_windows = self.driver.window_handles
            new_tab = [win for win in new_windows if win not in current_windows][0]
            self.driver.switch_to.window(new_tab)
        except TimeoutException:
            self._take_screenshot("new_tab_not_opened")
            self.fail("A new tab was not opened.")

        # Check the loading of the new page and the URL.
        try:
            WebDriverWait(self.driver, 20).until(
                EC.url_contains("jobs.lever.co/useinsider")
            )
        except TimeoutException:
            self._take_screenshot("lever_page_not_loaded")
            self.fail("The lever application form page did not open in time.")

        self.assertIn("jobs.lever.co/useinsider", self.driver.current_url)
        time.sleep(3)

