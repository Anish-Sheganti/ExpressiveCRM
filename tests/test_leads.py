from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_leads_tab():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080/espocrm/index.php")

    # login code (fill username, password, submit)
    driver.find_element(By.ID, "field-userName").send_keys("admin")
    driver.find_element(By.ID, "field-password").send_keys("Kavya@123")
    driver.find_element(By.ID, "login-button").click()

    # Wait for dashboard/homepage to load (optional)
    WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))

    # ---- Paste the snippet here ----
    leads_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Leads"))
    )
    leads_tab.click()

    leads_header = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Leads')]"))
    )

    assert leads_header.is_displayed(), "Leads page did not open successfully!"

    driver.quit()
