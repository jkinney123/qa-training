import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class TestTestcardpayment():
    def setup_method(self, method):
        options = Options()
        options.add_argument('--headless')  # Enable headless mode

        firefox_path = "/nix/store/w4k2jacmrlhasrnnflkl2p2xzq93nchg-firefox-127.0.2/bin/firefox"
        options.binary_location = firefox_path

        service = Service(executable_path='/nix/store/0qgkw2gg4kvdwnqxfwxyikcjq4p9ljsf-geckodriver-0.33.0/bin/geckodriver')
        self.driver = webdriver.Firefox(service=service, options=options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_testcardpayment(self):
        self.driver.get("https://weathershopper.pythonanywhere.com/")
        print("Navigated to Weather Shopper")

        self.driver.set_window_size(1440, 790)
        wait = WebDriverWait(self.driver, 10)

        # Click on the first button
        first_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-center:nth-child(1) .btn")))
        first_button.click()
        print("Clicked on the first button")

        # Click on the second button
        second_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".row:nth-child(2) > .text-center:nth-child(3) > .btn")))
        second_button.click()
        print("Clicked on the second button")

        # Click on the third button
        third_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-center:nth-child(5) > .btn")))
        third_button.click()
        print("Clicked on the third button")

        # Click on the 'Pay with Card' button
        pay_with_card = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".thin-text")))
        pay_with_card.click()
        print("Clicked on 'Pay with Card'")

        # Switch to the payment iframe
        iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[name^='stripe_checkout_app']")))
        print("Switched to payment iframe")

        # Fill in the email field
        email_field = wait.until(EC.element_to_be_clickable((By.ID, "email")))
        email_field.send_keys("testemail@example.com")
        print("Entered email")

        # Fill in the card number field
        card_number_field = wait.until(EC.element_to_be_clickable((By.ID, "card_number")))
        card_number_field.send_keys("4242 4242 4242 4242")
        print("Entered card number")

        # Fill in the expiration date field
        exp_field = wait.until(EC.element_to_be_clickable((By.ID, "cc-exp")))
        exp_field.send_keys("12 / 28")
        print("Entered expiration date")

        # Fill in the CVC field
        cvc_field = wait.until(EC.element_to_be_clickable((By.ID, "cc-csc")))
        cvc_field.send_keys("123")
        print("Entered CVC")

        # Fill in the ZIP code field
        zip_field = wait.until(EC.element_to_be_clickable((By.ID, "billing-zip")))
        zip_field.send_keys("56111")
        print("Entered billing ZIP code")

        # Click on the submit button
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        submit_button.click()
        print("Clicked on submit button")

        # Optionally, switch back to the default content
        self.driver.switch_to.default_content()
        print("Switched back to default content")

        # Verify successful payment or any subsequent steps
        # For example, check for a success message
        success_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".container div")))
        assert "PAYMENT SUCCESS" in success_message.text
        print("Payment was successful")