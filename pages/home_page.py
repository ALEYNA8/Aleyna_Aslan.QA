from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class HomePage:
    BODY_TAG = (By.TAG_NAME, "body")
    COMPANY_MENU = (By.XPATH, '//*[@id="navbarDropdownMenuLink"]')
    CAREERS_BUTTON = (By.XPATH, '//*[@id="navbarNavDropdown"]/ul[1]/li[6]/div/div[2]/a[2]')

    def __init__(self, driver):
        self.driver = driver

    # It moves the cursor to an empty spot on the page and turns off the effects.
    def hide_why_insider_hover(self):
        body = self.driver.find_element(*self.BODY_TAG)
        actions = ActionChains(self.driver)
        actions.move_to_element(body).perform()
        time.sleep(1)

    # Hovers the mouse over the company menu.
    def hover_company_menu(self):
        company_menu = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.COMPANY_MENU)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(company_menu).perform()
        time.sleep(1)

    # Clicks on the careers button.
    def click_careers(self):
        self.hide_why_insider_hover()
        self.hover_company_menu()
        careers_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CAREERS_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", careers_button)

    # It checks whether you are currently on the homepage.
    def is_on_home_page(self):
        return "useinsider.com" in self.driver.current_url

    # Accepts the cookie popup on the homepage.
    def accept_cookies_popup(self):
        try:
            accept_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, "wt-cli-accept-all-btn"))
            )
            accept_btn.click()
            print("✅ Cookies accepted on home page.")
        except:
            print("⚠ Cookies accept button not found or already accepted on home page.")

