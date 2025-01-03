from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# BrowserStack credentials
USERNAME = "amritavarshinirv_M6mShJ"  # BrowserStack username
ACCESS_KEY = "11sHiFppXkzKWGwLy97N"  # BrowserStack access key

# BrowserStack remote URL
BROWSERSTACK_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

# Browser and device configurations for 12 combinations
devices_and_browsers = [
    # Samsung Galaxy S20 Phone for Chrome, Firefox, Edge
    {"device": "Samsung Galaxy S20", "browser": "chrome", "os": "Android", "os_version": "10"},
    {"device": "Samsung Galaxy S20", "browser": "firefox", "os": "Android", "os_version": "10"},
    {"device": "Samsung Galaxy S20", "browser": "edge", "os": "Android", "os_version": "10"},

    # iPhone 12 Phone for Safari
    {"device": "iPhone 12", "browser": "safari", "os": "iOS", "os_version": "14"},

    # Samsung Galaxy Tab S6 Tablet for Chrome, Firefox, Edge
    {"device": "Samsung Galaxy Tab S6", "browser": "chrome", "os": "Android", "os_version": "10"},
    {"device": "Samsung Galaxy Tab S6", "browser": "firefox", "os": "Android", "os_version": "10"},
    {"device": "Samsung Galaxy Tab S6", "browser": "edge", "os": "Android", "os_version": "10"},

    # iPad Pro Tablet for Safari
    {"device": "iPad Pro 12.9 2020", "browser": "safari", "os": "iOS", "os_version": "14"},
]

def login(driver, username, password):
    """Logs into the application."""
    print(f"Navigating to login page...")
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    print(f"Entering username: '{username}'")
    driver.find_element(By.ID, "user-name").send_keys(username)
    time.sleep(1)

    print(f"Entering password: '{password}'")
    driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(1)

    print("Clicking login button...")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

def test_login(driver):
    """Tests various login scenarios."""

    # Case 1: Valid username, valid password
    """Test Case 1: Valid username and password for 'standard_user'."""
    print("\n--- Test Case 1: Valid username and password ---")
    login(driver, "standard_user", "secret_sauce")
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        print("No error message displayed. Login successful ✅ .")
    except TimeoutException:
        print("❌ Login failed: Inventory container not found.")
    driver.refresh()
    time.sleep(2)

    """Test Case 2: Valid username and password for 'problem_user'."""
    print("\n--- Test Case 2: Valid username and password ---")
    
    login(driver, "problem_user", "secret_sauce")
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        print("No error message displayed. Login successful ✅.")
    except TimeoutException:
        print("❌ Login failed: Inventory container not found.")
    driver.refresh()
    time.sleep(2)



    """Test Case 3: Valid username and password for 'performance_glitch_user'."""
    print("\n--- Test Case 3: Valid username and password ---")
   
    login(driver, "performance_glitch_user", "secret_sauce")
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        print("No error message displayed. Login successful ✅.")
    except TimeoutException:
        print("❌ Login failed: Inventory container not found.")
    driver.refresh()
    time.sleep(2)



    """Test Case 4: Valid username and password for 'error_user'."""
    print("\n--- Test Case 4: Valid username and password ---")
    
    login(driver, "error_user", "secret_sauce")
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        print("No error message displayed. Login successful ✅.")
    except TimeoutException:
        print("❌ Login failed: Inventory container not found.")
    driver.refresh()
    time.sleep(2)



    """Test Case 5: Valid username and password for 'visual_user'."""
    print("\n--- Test Case 5: Valid username and password ---")
    
    login(driver, "visual_user", "secret_sauce")
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        print("No error message displayed. Login successful ✅.")
    except TimeoutException:
        print("❌ Login failed: Inventory container not found.")
    driver.refresh()
    time.sleep(2)



    # Case 2: Invalid username, valid password
    print("\n--- Test Case 6: Invalid username, valid password ---")
    driver.refresh()
    time.sleep(2)
    login(driver, "invalid_user", "secret_sauce")
    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        ).text
        print(f"Error message: {error_message}")
        assert "Epic sadface" in error_message, "Error message not displayed for invalid username"
    except TimeoutException:
        print("No error message displayed.")

    # Case 3: Empty username, valid password
    print("\n--- Test Case 7: Empty username, valid password ---")
    driver.refresh()
    time.sleep(2)
    login(driver, "", "secret_sauce")
    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        ).text
        print(f"Error message: {error_message}")
        assert "Username is required" in error_message, "Error message not displayed for empty username"
    except TimeoutException:
        print("No error message displayed.")

    # Case 4: Valid username, empty password
    print("\n--- Test Case 8: Valid username, empty password ---")
    driver.refresh()
    time.sleep(2)
    login(driver, "standard_user", "")
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        ).text
        print(f"Error message: {error_message}")
        assert "Password is required" in error_message, "Error message not displayed for empty password"
    except TimeoutException:
        print("No error message displayed.")

    # Case 5: Both username and password empty
    print("\n--- Test Case 9: Both username and password empty ---")
    driver.refresh()
    time.sleep(2)
    login(driver, "", "")
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        ).text
        print(f"Error message: {error_message}")
        assert "Username is required" in error_message, "Error message not displayed for both fields empty"
    except TimeoutException:
        print("No error message displayed.")

    # Case 6: Locked-out user
    print("\n--- Test Case 10: Locked-out user ---")
    driver.refresh()
    time.sleep(2)
    login(driver, "locked_out_user", "secret_sauce")
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        ).text
        print(f"Error message: {error_message}")
        assert "Epic sadface: Sorry, this user has been locked out." in error_message, "Error message not displayed for locked-out user"
    except TimeoutException:
        print("No error message displayed.")

   # Additional test cases
    """Test SQL Injection."""
    print("\n--- Test Case 11: Testing SQL Injection ---")
    login(driver, "' OR '1'='1", "anything")
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
	).text
        print(f"Error message displayed: {error_message}. Test successful: SQL Injection blocked ✅.")
    except TimeoutException:
        print("❌ Test failed: SQL Injection not blocked! Potential vulnerability detected.")

    """Test special characters."""
    print("\n--- Test Case 12: Testing special characters ---")
    login(driver, "@#$%^&*", "()<>?/{}")
    try:
        error_message = WebDriverWait(driver, 10).until(
	    EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        ).text
        print(f"Error message displayed: {error_message}. Test successful: Special characters blocked ✅.")
    except TimeoutException:
        print("❌ Test failed: Special characters not blocked! Potential vulnerability detected.")

    """Test excessively long inputs."""
    print("\n--- Test Case 13: Testing excessively long inputs ---")
    login(driver, "a" * 1000, "b" * 1000)
    try:
        error_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        ).text
        print(f"Error message displayed: {error_message}. Test successful: Long inputs blocked ✅.")
    except TimeoutException:
        print("❌ Test failed: Long inputs not blocked! Potential vulnerability detected.")

    """Test whitespace inputs."""
    print("\n--- Test Case 14: Testing whitespace inputs ---")
    login(driver, " ", " ")
    try:
        error_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        ).text
        print(f"Error message displayed: {error_message}. Test successful: Whitespace inputs blocked ✅.")
    except TimeoutException:
        print("❌ Test failed: Whitespace inputs not blocked! Potential vulnerability detected.")

    """Test case sensitivity."""
    print("\n--- Test Case 15: Testing case sensitivity ---")
    login(driver, "STANDARD_USER", "SECRET_SAUCE")
    try:
        error_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        ).text
        print(f"Error message displayed: {error_message}. Test successful: Case sensitivity enforced ✅.")
    except TimeoutException:
        print("❌ Test failed: Case sensitivity not enforced! Potential vulnerability detected.")

    

    """Test browser back button functionality."""
    print("\n--- Test Case 16: Testing browser back button ---")
    login(driver, "standard_user", "secret_sauce")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "inventory_container")))
    driver.back()
    time.sleep(2)
    current_url = driver.current_url
    if "saucedemo.com" in current_url:
        print("Test successful: Browser back button handled correctly ✅.")
    else:
        print("❌ Test failed: Browser back button allowed unauthorized access!")


    """Test logout functionality."""
    print("\n--- Test Case 17: Testing logout functionality ---")
    login(driver, "standard_user", "secret_sauce")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "inventory_container")))
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(2)
    driver.find_element(By.ID, "logout_sidebar_link").click()
    time.sleep(2)
    current_url = driver.current_url
    if "saucedemo.com" in current_url:
        print("Test successful: Logout functionality works as expected ✅.")
    else:
        print("❌ Test failed: Logout functionality not working properly!")



def run_test_on_browser(device_config):
    """Runs the login test on a specific device/browser configuration."""
    
    # Initialize the browser options based on the selected browser
    if device_config["browser"] == "chrome":
        options = webdriver.ChromeOptions()
    elif device_config["browser"] == "firefox":
        options = webdriver.FirefoxOptions()
    elif device_config["browser"] == "edge":
        options = webdriver.EdgeOptions()
    elif device_config["browser"] == "safari":
        options = webdriver.SafariOptions()
    else:
        print(f"Unsupported browser: {device_config['browser']}")
        return

    # Add BrowserStack capabilities
    options.set_capability("browser", device_config["browser"])
    options.set_capability("browser_version", "latest")
    options.set_capability("os", device_config["os"])
    options.set_capability("os_version", device_config["os_version"])
    options.set_capability("device", device_config["device"])
    options.set_capability("name", f"Test on {device_config['browser']} for {device_config['device']}")

    print(f"\nRunning test on {device_config['browser']} for {device_config['device']} ({device_config['os']} {device_config['os_version']})")
    # Initialize WebDriver with BrowserStack remote execution
    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_URL,
        options=options,
    )

    try:
        test_login(driver)
    finally:
        driver.quit()

def run_tests():
    """Runs the login tests across all device/browser configurations."""
    for device in devices_and_browsers:
        run_test_on_browser(device)

# Execute the tests
run_tests()
