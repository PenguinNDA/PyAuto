import math
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Create our variable
link = "http://suninjuly.github.io/find_link_text"
number = str(math.ceil(math.pow(math.pi, math.e)*10000))
browser = webdriver.Chrome(ChromeDriverManager().install())

try:

    # Open browser
    browser.get(link)

    # Find our number and click it
    link = browser.find_element(By.PARTIAL_LINK_TEXT, number)
    link.click()

    # Input our data to text fields
    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    # Click to button
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:

    # waiting 30 sec for copy code
    time.sleep(5)

    # close browser
    browser.quit()
