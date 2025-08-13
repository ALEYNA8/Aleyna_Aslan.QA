import time
from selenium.common import TimeoutException
from tests.base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.career_page import CareerPage
from pages.page_check import career_page_check, home_page_check

class InsiderTest(BaseTest):

    def test_career_page_navigation(self):
        self.driver.get("https://useinsider.com/")
        home_page = HomePage(self.driver)

        # Homepage visibility controls
        home_page_check(home_page)
        time.sleep(2)

        # Cookie acceptance on the homepage using page method
        home_page.accept_cookies_popup()

        # Transition to the career page
        home_page.click_careers()
        WebDriverWait(self.driver, 10).until(EC.url_contains("careers"))
        self.assertIn("careers", self.driver.current_url, "Not on Careers page!")

        career_page = CareerPage(self.driver)

        # Career page visibility checks
        career_page_check(career_page)
        time.sleep(2)

        # Go to the Quality Assurance page and perform the filtering operations.
        career_page.go_to_quality_assurance_page()
        career_page.accept_cookies_popup()
        career_page.click_see_all_qa_jobs()
        WebDriverWait(self.driver, 10).until(EC.url_contains("open-positions"))
        self.assertIn("open-positions", self.driver.current_url)
        time.sleep(2)

        current_windows = self.driver.window_handles

        # Hover over the 'View Role' button on the job advertisement and click it.
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

        # Load the new page and verify the URL.
        try:
            WebDriverWait(self.driver, 20).until(
                EC.url_contains("jobs.lever.co/useinsider")
            )
        except TimeoutException:
            self._take_screenshot("lever_page_not_loaded")
            self.fail("The lever application form page did not open in time.")

        self.assertIn("jobs.lever.co/useinsider", self.driver.current_url)
        time.sleep(3)


