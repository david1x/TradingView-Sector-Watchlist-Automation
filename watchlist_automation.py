# Updated watchlist_automation.py

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Connect to Selenium Grid
hub_url = 'http://your-selenium-grid-url/wd/hub'

# Example of desired capabilities for a Chrome browser
capabilities = DesiredCapabilities.CHROME.copy()

# Create a remote WebDriver instance
driver = webdriver.Remote(command_executor=hub_url, desired_capabilities=capabilities)

# Your existing code

# Remember to quit the driver at the end
# driver.quit()