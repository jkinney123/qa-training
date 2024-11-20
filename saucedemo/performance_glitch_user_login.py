# Modified test_sauceperformanceglitch.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

def test_sauceperformanceglitch():
    # Set up Firefox options
    options = Options()
    # Uncomment the next line to run in headless mode
    options.add_argument('--headless')
    
    # Initialize the Firefox driver
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    
    try:
        # Start timing
        start_time = time.perf_counter()
        
        # Navigate to the login page
        driver.get("https://www.saucedemo.com/")
        print("Opened saucedemo.com")
        
        # Enter username
        driver.find_element(By.ID, "user-name").send_keys("performance_glitch_user")
        print("Entered username")
        
        # Enter password
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        print("Entered password")
        
        # Click login
        driver.find_element(By.ID, "login-button").click()
        print("Clicked login button")
        
        # Wait for the inventory page to load
        time.sleep(2)  # Simple wait; can be replaced with explicit waits
        
        # Verify login success
        try:
            driver.find_element(By.ID, "inventory_container")
            print("Login successful as performance_glitch_user.")
        except NoSuchElementException:
            print("Login failed for performance_glitch_user.")
        
        # End timing
        end_time = time.perf_counter()
        login_time = end_time - start_time
        print(f"Login time for performance_glitch_user: {login_time:.2f} seconds.")
    
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_sauceperformanceglitch()
