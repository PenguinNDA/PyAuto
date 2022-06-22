from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Create our variable
link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome(ChromeDriverManager().install())

try:

    # Open browser
    browser.get(link)

    # Input our data to text fields
    input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    input1.send_keys("Send")

    input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    input2.send_keys("Text?")

    input3 = browser.find_element(By.CLASS_NAME, 'third')
    input3.send_keys("send@text.qa")

    # press button "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Check result
    # Waiting for page open
    time.sleep(1)

    # Find element with text
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    welcome_text = welcome_text_elt.text

    # with assert check welcome_text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    # Waiting 10 sec for see result
    time.sleep(10)

    # close browser
    browser.quit()
