from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('--headless')  # Enable headless mode

# Optional: If geckodriver is not in your PATH
service = Service(executable_path=r'C:\Users\joeki\Drivers\geckodriver.exe')

driver = webdriver.Firefox(options=options)  # Or with service: driver = webdriver.Firefox(service=service, options=options)

driver.get("https://www.python.org")
title = driver.title
print(f"Page title: {title}")

driver.quit()