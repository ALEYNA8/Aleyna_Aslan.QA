import time
import os
from selenium.common import TimeoutException
from tests.base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.career_page import CareerPage
from pages.page_check import career_page_check, home_page_check

class InsiderTest(BaseTest):

    def test_full_flow(self):
        self.driver.get("https://useinsider.com/")
        home_page = HomePage(self.driver)

        home_page_check(home_page)

        time.sleep(2)

        try:
            accept_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, "wt-cli-accept-all-btn"))
            )
            accept_btn.click()
            print("✅ Cookies accepted on home page.")
        except:
            print("Cookies accept button not found or already accepted on home page.")

        home_page.click_careers()
        WebDriverWait(self.driver, 10).until(EC.url_contains("careers"))
        self.assertIn("careers", self.driver.current_url, "Not on Careers page!")

        career_page = CareerPage(self.driver)

        career_page_check(career_page)

        time.sleep(2)

        career_page.go_to_quality_assurance_page()
        career_page.accept_cookies_popup()
        career_page.click_see_all_qa_jobs()
        WebDriverWait(self.driver, 10).until(EC.url_contains("open-positions"))
        self.assertIn("open-positions", self.driver.current_url)

        time.sleep(2)

        current_windows = self.driver.window_handles

        try:
            career_page.hover_and_click_first_view_role()
        except TimeoutException:
            self._take_screenshot("view_role_button_not_clickable")
            self.fail("The View Role button was not found or could not be clicked.")

        try:
            WebDriverWait(self.driver, 20).until(lambda d: len(d.window_handles) > len(current_windows))
            new_windows = self.driver.window_handles
            new_tab = [win for win in new_windows if win not in current_windows][0]
            self.driver.switch_to.window(new_tab)
        except TimeoutException:
            self._take_screenshot("new_tab_not_opened")
            self.fail("A new tab was not opened.")

        try:
            WebDriverWait(self.driver, 20).until(
                EC.url_contains("jobs.lever.co/useinsider")
            )
        except TimeoutException:
            self._take_screenshot("lever_page_not_loaded")
            self.fail("The lever application form page did not open in time.")

        self.assertIn("jobs.lever.co/useinsider", self.driver.current_url)
        time.sleep(3)

