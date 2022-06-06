import time

# webdriver we're using for communicate with browser
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

# use pause for 5 seconds
time.sleep(5)

# open site by get
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# Method find_element use for search element on page
# Search text area
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

# Typing text from answer
textarea.send_keys("get()")
time.sleep(5)

# Find button
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# Click button
submit_button.click()
time.sleep(5)

# Close browser
driver.quit()
