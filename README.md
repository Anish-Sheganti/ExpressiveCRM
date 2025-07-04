# 🧪 ExpressiveCRM - Selenium Automation Suite

This project is an **End-to-End Selenium Automation Test Suite** built using **Python, Selenium, and Pytest** to test the core functionality of the **EspoCRM** application. It includes automated flows for login, navigation, and lead module verification.

---

## 🚀 Tech Stack

 ![Python](https://img.shields.io/badge/python-3.11-blue.svg?logo=python)
![Selenium](https://img.shields.io/badge/selenium-4.20.0-brightgreen.svg?logo=selenium)
![PyTest](https://img.shields.io/badge/pytest-8.1.1-yellow.svg?logo=pytest)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-blue?logo=github)
![HTML Report](https://img.shields.io/badge/report-html-orange)


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


