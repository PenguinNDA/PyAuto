import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(ChromeDriverManager().install())
link = "http://suninjuly.github.io/wait1.html"

try:

    # Open browser
    browser.get(link)

    # Wait 1 sec
    time.sleep(1)

    # Click to button
    button = browser.find_element(By.ID, "verify")
    button.click()

    # Find our text
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:

    # Waiting 10 sec for see result
    time.sleep(10)
    # close browser
    browser.quit()
