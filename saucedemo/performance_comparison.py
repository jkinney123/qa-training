# Combined script: test_login_performance_comparison.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

def measure_login_time(username):
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
        print(f"Opened saucedemo.com for {username}")
        
        # Enter username
        driver.find_element(By.ID, "user-name").send_keys(username)
        print(f"Entered username: {username}")
        
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
            print(f"Login successful as {username}.")
        except NoSuchElementException:
            print(f"Login failed for {username}.")
            return None
        
        # End timing
        end_time = time.perf_counter()
        login_time = end_time - start_time
        print(f"Login time for {username}: {login_time:.2f} seconds.\n")
        return login_time
    
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    # Measure login time for standard_user
    standard_user_time = measure_login_time("standard_user")
    
    # Measure login time for performance_glitch_user
    performance_glitch_user_time = measure_login_time("performance_glitch_user")
    
    # Compare login times
    if standard_user_time is not None and performance_glitch_user_time is not None:
        time_difference = performance_glitch_user_time - standard_user_time
        print(f"Standard User Login Time: {standard_user_time:.2f} seconds")
        print(f"Performance Glitch User Login Time: {performance_glitch_user_time:.2f} seconds")
        print(f"Time Difference: {time_difference:.2f} seconds")
    else:
        print("Could not measure login times for both users.")
