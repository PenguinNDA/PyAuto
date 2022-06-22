from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Create our variable
browser = webdriver.Chrome(ChromeDriverManager().install())
link = "http://suninjuly.github.io/huge_form.html"

try:

    # Open browser
    browser.get(link)

    # Find some elements by Tag 'input' and for every element type 'lokodoco'
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("lokodoco")

    # Find button and click it
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:

    # Waiting 30 seconds for answer and copy code
    time.sleep(30)

    # Close browser after all
    browser.quit()
