from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Waits for the element to come in up to 10 seconds.

    def find(self, locator):
        """Waits for and finds the element with the given locator."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def visit(self, url):
        """ Goes to the given URL. """
        self.driver.get(url)

    def get_title(self):
        """ Returns the title information of the current page. """
        return self.driver.title