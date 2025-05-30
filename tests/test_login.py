from selenium.webdriver.common.by import By
from utils.driver_setup import get_driver   # <--- This line is REQUIRED

def test_login():
    driver = get_driver()
    driver.get("http://localhost:8080/espocrm")

    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    print("Current URL after login:", driver.current_url)  # To debug

    assert "/espocrm/" in driver.current_url.lower()

    driver.quit()


