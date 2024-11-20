from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary




options = Options()
options.add_argument('--headless')  # Enable headless mode

firefox_path = "/nix/store/w4k2jacmrlhasrnnflkl2p2xzq93nchg-firefox-127.0.2/bin/firefox"  # Replace with the actual path

# Create FirefoxBinary Object
binary = FirefoxBinary(firefox_path=firefox_path)
#Add binary location to options
options.binary_location = firefox_path

# Optional: If geckodriver is not in your PATH
service = Service(executable_path='/nix/store/0qgkw2gg4kvdwnqxfwxyikcjq4p9ljsf-geckodriver-0.33.0/bin/geckodriver') 
driver = webdriver.Firefox(service=service, options=options)


driver.get("https://www.python.org")
title = driver.title
print(f"Page title: {title}")

driver.quit()