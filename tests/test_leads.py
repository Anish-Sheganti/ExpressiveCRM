from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_leads_tab(driver):
    print("Opening EspoCRM login page...")
    driver.get("http://localhost:8080/espocrm/")

    print("Waiting for login form...")
    username_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "field-userName"))
    )
    password_field = driver.find_element(By.ID, "field-password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    print("Entering credentials and logging in...")
    username_field.send_keys("admin")
    password_field.send_keys("Kavya@123")
    login_button.click()

    print("Waiting after login...")
    time.sleep(3)  # Optional debug wait

    print("Waiting for Leads tab to appear...")
    leads_tab = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Leads"))  # Try this first
    )
    leads_tab.click()
