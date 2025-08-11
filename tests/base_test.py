import os
import time
import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):

    # Before the test starts, it launches the Chrome browser and maximizes the window.
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # Checks for errors after the test, takes a screenshot if there are any errors, and closes the browser.
    def tearDown(self):
        outcome = getattr(self, '_outcome', None)
        errors = []

        if outcome:
            if hasattr(outcome, 'errors'):
                errors = outcome.errors
            elif hasattr(outcome, 'result') and outcome.result:
                errors = outcome.result.errors or []

        for method, error in errors:
            if error:
                self._take_screenshot(self._testMethodName)
                break  #Take a screenshot only once.

        self.driver.quit()

    # It takes a screenshot and saves it in the 'screenshots' folder.
    def _take_screenshot(self, name_prefix):
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        file_path = os.path.join(screenshot_dir, f"{name_prefix}_{timestamp}.png")
        self.driver.save_screenshot(file_path)
        print(f" Screenshot saved to {file_path}")

