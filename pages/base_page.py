# The BasePage class provides basic page operations and the waiting mechanism.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    # Starts the driver and the waiting object.
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Waits for the element to be visible on the page with the specified locator and returns.
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    # Goes to the given URL.
    def visit(self, url):
        self.driver.get(url)

    # Returns the title of the current page.
    def get_title(self):
        return self.driver.title
