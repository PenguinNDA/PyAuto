from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import math
import time

# Create our variable
link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome(ChromeDriverManager().install())


# Some math tricks
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    # Open browser
    browser.get(link)

    # Take value from text field
    x_element = browser.find_element(By.ID, 'input_value')
    math_x = x_element.text

    # Use math tricks
    math_y = calc(math_x)

    # Input our data to text fields
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(math_y)

    # Click to checkbox
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    # Click to radio button
    radioButton = browser.find_element(By.ID, 'robotsRule')
    radioButton.click()

    # press button "Submit"
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:

    # Waiting 10 sec for see result
    time.sleep(10)

    # close browser
    browser.quit()
