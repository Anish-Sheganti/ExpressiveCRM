# 🚀 Expressive CRM - Selenium Automation Project

This is a QA Automation project for **EspoCRM** using **Python + Selenium**. It demonstrates UI test automation for login and lead management features.

## 🧪 Features Covered

- ✅ Login test with valid credentials
- ✅ Lead creation test
- ✅ Driver setup using `webdriver-manager`
- ✅ Page source saved after login
- ✅ Test scripts organized in folders

## 📁 Folder Structure

ExpressiveCRM/
│
├── tests/
│ ├── test_login.py
│ └── test_leads.py
│
├── utils/
│ └── driver_setup.py
│
├── espocrm_login.py
├── page_source_after_login.html
├── requirements.txt
└── README.md

bash
Copy
Edit

## 🛠️ Technologies Used

- Python
- Selenium
- WebDriver Manager
- PyTest (optional for scaling tests)
- Git & GitHub

## 🚀 Run the Project

```bash
# Install all dependencies
pip install -r requirements.txt

# Run individual test scripts
python espocrm_login.py
python tests/test_login.py
python tests/test_leads.py

🧑‍💼 Author
Kavyasri Singam
