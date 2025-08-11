from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Move the mouse over the body to remove the hover effect on the page.
    def hide_why_insider_hover(self):
        body = self.driver.find_element(By.TAG_NAME, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(body).perform()
        time.sleep(1)

    # Hover over the company menu with the mouse.
    def hover_company_menu(self):
        company_locator = (By.XPATH, '//*[@id="navbarDropdownMenuLink"]')
        company_menu = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(company_locator)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(company_menu).perform()
        time.sleep(1)

    # Takes the necessary actions to click the Careers button.
    def click_careers(self):
        self.hide_why_insider_hover()
        self.hover_company_menu()
        careers_locator = (By.XPATH, '//*[@id="navbarNavDropdown"]/ul[1]/li[6]/div/div[2]/a[2]')
        careers_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(careers_locator)
        )
        self.driver.execute_script("arguments[0].click();", careers_button)

    # Checks if you are currently on the homepage.
    def is_on_home_page(self):
        return "useinsider.com" in self.driver.current_url
