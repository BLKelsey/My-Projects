from selenium import webdriver                                    # Main Selenium browser controller
from selenium.webdriver.common.by import By                       # Used to locate elements (id, text, xpath, etc.)
from selenium.webdriver.support.ui import WebDriverWait           # Allows waiting for conditions
from selenium.webdriver.support import expected_conditions as EC  # Common wait conditions
import time                                                       # Used for pauses (sleep)

# ─────────────────────────────
# Start browser
# ─────────────────────────────
driver = webdriver.Chrome()                         # Launch a new Chrome browser
driver.get("https://thefederalist.com")             # Open the Federalist homepage

# Make sure page loads
WebDriverWait(driver, 10).until(                    # Wait up to 10 seconds until condition is met
    EC.presence_of_element_located((By.TAG_NAME, "body"))  # Page body exists = page loaded
)

driver.maximize_window()                            # Maximize browser window (avoid mobile layout)
print("Home page loaded")                           # Console message for debugging

# ─────────────────────────────
# Click "Latest"
# ─────────────────────────────
latest_link = WebDriverWait(driver, 15).until(      # Wait up to 15 seconds for the link
    EC.element_to_be_clickable(                            # Ensure the link can actually be clicked
        (By.XPATH, "//a[normalize-space()='Latest']")      # Find link with visible text "Latest"
    )
)

print("Clicking Latest...")                          # Debug message
latest_link.click()                                  # Click the "Latest" link

# ─────────────────────────────
# Verify navigation
# ─────────────────────────────
WebDriverWait(driver, 15).until(                    # Wait until navigation finishes
    EC.url_contains("latest")
    # URL must contain "latest"
)

print("Latest page loaded")                          # Confirmation message

# ─────────────────────────────
# Slow scrolling
# ─────────────────────────────
print("Starting slow scroll...")                    # Debug message

for i in range(8):                                   # Repeat scrolling 8 times
    driver.execute_script("window.scrollBy(0, 90);")  # Scroll down 70 pixels
    time.sleep(1)                                     # Wait 3 second between scrolls

print("Scrolling finished")                         # Scroll complete

# ─────────────────────────────
# Keep browser open
# ─────────────────────────────
input("Press ENTER to close the browser...")        # Pause script until user presses Enter
driver.quit()                                       # Close the browser cleanly
