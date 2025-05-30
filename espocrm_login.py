from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Step 1: Setup Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Step 2: Open EspoCRM login page
driver.get("http://localhost:8080/espocrm")  # Use http://localhost:8080/espocrm if using port 8080

# Step 3: Wait for page to load
time.sleep(3)

# Step 4: Enter login credentials
driver.find_element(By.NAME, "username").send_keys("admin")  # Replace with your actual username
driver.find_element(By.NAME, "password").send_keys("Kavya@123")  # Replace with your actual password

# Step 5: Click the login button
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Step 6: Wait to see the result
time.sleep(5)

# Optional: Validate login success by checking for "Home" tab or dashboard
if "EspoCRM" in driver.title or "Home" in driver.page_source:
    print("✅ Login successful!")
else:
    print("❌ Login failed!")

# Step 7: Close the browser
driver.quit()
