# 🧪 ExpressiveCRM - Selenium Automation Suite

This project is an **End-to-End Selenium Automation Test Suite** built using **Python, Selenium, and Pytest** to test the core functionality of the **EspoCRM** application. It includes automated flows for login, navigation, and lead module verification.

---

## 🚀 Tech Stack

- 🐍 Python 3.13
- 🧪 Selenium WebDriver
- ✅ Pytest
- 🧾 Pytest-HTML (for reporting)
- 🌐 Google Chrome (via ChromeDriver)

---

## ✅ Features Tested

- 🔐 Login functionality with valid credentials
- 🧭 Navigation to the **Leads** module
- 📋 Validation of UI elements in Leads tab

---

## 🧪 Test Scenarios

| Test File         | Description                          | Status  |
|------------------|--------------------------------------|---------|
| `test_login.py`  | Verifies login page and dashboard    | ✅ Pass |
| `test_leads.py`  | Validates navigation to Leads tab    | ✅ Pass |

---

## 🛠️ How to Run Tests Locally

1. **Install dependencies**  
   *(inside your virtual environment if you're using one)*

   pip install -r requirements.txt
Start local EspoCRM server
Make sure XAMPP is running and http://localhost:8080/espocrm/ is accessible.

Run tests with HTML report

pytest tests/ --html=report.html
View test report
Open report.html in your browser.

📂 Project Structure

ExpressiveCRM/
├── tests/
│   ├── test_login.py
│   └── test_leads.py
├── conftest.py
├── report.html
├── requirements.txt
└── README.md

✍️ Author
KavyaSri Singam
