from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup():
    # Configure Firefox options
    options = Options()
    options.add_argument('--headless')

    # Initialize the Firefox driver
    return webdriver.Firefox(options=options)

def test_python_website():
    driver = setup()

    # Connect to the website under test
    driver.get("http://www.python.org")

    # Make an assertion (true/false)
    assert "Python" in driver.title

    # Get the Searchbar
    elem = driver.find_element(By.NAME, "q")

    # Clear the Searchbar
    elem.clear()

    # Simulate pressing the p, y, c, o, n keys on the keyboard
    elem.send_keys("pycon")

    # Simulate hitting the Enter key on the keyboard
    elem.send_keys(Keys.RETURN)

    # Make an assertion (true/false)
    assert "No results found." not in driver.page_source

    print('Python Website Test Successful')

    # Close the browser
    driver.close()
    driver.quit()

def test_weathershopper_temperature():
    driver = setup()

    url = "https://weathershopper.pythonanywhere.com/"
    driver.get(url)
    print(f"\nStarting at: {url}")

    # Get the element that houses the temperature value using its ID
    temperature = driver.find_element(By.ID, "temperature").text

    # Get the temperature string value from the element
    print(f"The temperature is {temperature}.")

    # Remove celsius from the string so we can convert it to an integer
    temperatureValueOnly = int(temperature.split(" ")[0])
    print(f"The temperature value is {temperatureValueOnly}.")

    # Decide which product to buy based on temperature
    if temperatureValueOnly > 19:
        print('Temperature was ABOVE 19 C: Clicking the Sunscreens button')
        buySunscreensButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Buy sunscreens')]")
        buySunscreensButton.click()
        product_type = 'sunscreen'
    else:
        print('Temperature was BELOW 19 C: Clicking the Moisturizers button')
        buyMoisturizersButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Buy moisturizers')]")
        buyMoisturizersButton.click()
        product_type = 'moisturizer'

    print(f'Current webpage: {driver.current_url}.')
    assert driver.current_url == f"https://weathershopper.pythonanywhere.com/{product_type}"

    print('Weather Shopper Landing Page Test Successful')

    # Return the driver and product type for the next steps
    return driver, product_type

def test_weathershopper_product_page(driver, product_type):
    # We are already on the correct product page
    print(f"\nStarting at: {driver.current_url}")

    # Retrieve all product cards
    products = driver.find_elements(By.CLASS_NAME, "col-4")

    # Variables to store the least expensive products
    if product_type == 'sunscreen':
        # For sunscreens, we look for SPF-50 and SPF-30
        cheapest_spf50_button = None
        cheapest_spf50_price = float("inf")
        cheapest_spf30_button = None
        cheapest_spf30_price = float("inf")
    elif product_type == 'moisturizer':
        # For moisturizers, we look for Aloe and Almond
        cheapest_aloe_button = None
        cheapest_aloe_price = float("inf")
        cheapest_almond_button = None
        cheapest_almond_price = float("inf")

    # Loop through each product card
    for product in products:
        name = product.find_element(By.TAG_NAME, "p").text
        print(f"Product name: {name}")
        price_text = product.find_elements(By.TAG_NAME, "p")[1].text
        price = int(price_text.split(" ")[-1].strip())
        print(f"Price: {price}")
        button = product.find_element(By.TAG_NAME, "button")

        if product_type == 'sunscreen':
            if "SPF-50" in name and price < cheapest_spf50_price:
                cheapest_spf50_price = price
                cheapest_spf50_button = button
            elif "SPF-30" in name and price < cheapest_spf30_price:
                cheapest_spf30_price = price
                cheapest_spf30_button = button
        elif product_type == 'moisturizer':
            if "Aloe" in name and price < cheapest_aloe_price:
                cheapest_aloe_price = price
                cheapest_aloe_button = button
            elif "Almond" in name and price < cheapest_almond_price:
                cheapest_almond_price = price
                cheapest_almond_button = button

    # Add the least expensive products to the cart
    if product_type == 'sunscreen':
        if cheapest_spf50_button:
            cheapest_spf50_button.click()
        if cheapest_spf30_button:
            cheapest_spf30_button.click()
        print(f"The least expensive SPF-50 sunscreen is: {cheapest_spf50_price}")
        print(f"The least expensive SPF-30 sunscreen is: {cheapest_spf30_price}")
    elif product_type == 'moisturizer':
        if cheapest_aloe_button:
            cheapest_aloe_button.click()
        if cheapest_almond_button:
            cheapest_almond_button.click()
        print(f"The least expensive Aloe moisturizer is: {cheapest_aloe_price}")
        print(f"The least expensive Almond moisturizer is: {cheapest_almond_price}")

    # Click on the Cart button
    print('\nAdding them to the Cart.')
    cart_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Cart')]")
    cart_button.click()
    
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/cart"))
    print(f"Current URL after clicking cart: {driver.current_url}")

    # Proceed to payment
    test_weathershopper_payment(driver)

def test_weathershopper_payment(driver):
    wait = WebDriverWait(driver, 10)

    # Print the current URL
    print(f"Current URL before payment: {driver.current_url}")
    # Verify items are in the cart
    cart_items = driver.find_elements(By.CSS_SELECTOR, "table.table tbody tr")
    print(f"Number of items in cart: {len(cart_items)}")
    if len(cart_items) == 0:
        print("No items found in the cart.")
        driver.quit()
        return
    # Click on the 'Pay with Card' button
    pay_with_card = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".stripe-button-el")))
    pay_with_card.click()
    print("Clicked on 'Pay with Card'")

    with open("cart_page.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("Saved cart page source to cart_page.html")

    # Switch to the payment iframe
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[name^='stripe_checkout_app']")))
    print("Switched to payment iframe")

    # Fill in the payment form
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='email']"))).send_keys("testemail@example.com")
    print("Entered email")

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Card number']"))).send_keys("4242 4242 4242 4242")
    print("Entered card number")

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='MM / YY']"))).send_keys("12 / 28")
    print("Entered expiration date")

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='CVC']"))).send_keys("123")
    print("Entered CVC")


    # Switch to ZIP code iframe
    zip_iframe = driver.find_element(By.CSS_SELECTOR, "iframe[name='postal']")
    driver.switch_to.frame(zip_iframe)
    print("Switched to ZIP code iframe")

    # Enter ZIP code
    zip_field = wait.until(EC.element_to_be_clickable((By.NAME, "postal")))
    zip_field.send_keys("12345")
    print("Entered ZIP code")

    # Switch back to main payment iframe
    driver.switch_to.parent_frame()

    # Click on the submit button
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    print("Clicked on submit button")

    # Switch back to the default content
    driver.switch_to.default_content()
    print("Switched back to default content")

    # Verify successful payment
    success_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".container h2")))
    assert "PAYMENT SUCCESS" in success_message.text
    print("Payment was successful")

    # Close the browser
    driver.close()
    driver.quit()

# Use this to print out the HTML of the web page you
# are writing a test for. Useful for identifying how you 
# will fetch specific elements etc.
def show_me_the_html(url):
    driver = setup()
    driver.get(url)
    print(driver.page_source)
    driver.close()
    driver.quit()

# Run the tests
test_python_website()
driver, product_type = test_weathershopper_temperature()
test_weathershopper_product_page(driver, product_type)
