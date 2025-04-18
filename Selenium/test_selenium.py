from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Chrome Driver Setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Google
driver.get("https://www.allduniv.ac.in/")

# Print title
print("Page title:", driver.title)

# Close the browser
driver.quit()
