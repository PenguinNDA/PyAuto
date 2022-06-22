from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
link = "https://SunInJuly.github.io/execute_script.html"


# Some math tricks
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    # Open browser
    browser.get(link)

    # Find number
    math_x = browser.find_element(By.ID, 'input_value').text

    # Use math tricks
    math_y = calc(int(math_x))

    # Input our data to text fields
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(math_y)

    # Find button
    button = browser.find_element(By.TAG_NAME, "button")

    # Scroll page down
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Click to checkbox
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    # Click to radio button
    radioButton = browser.find_element(By.ID, 'robotsRule')
    radioButton.click()

    # Click to button
    button.click()

finally:

    # Waiting 10 sec for see result
    time.sleep(10)

    # close browser
    browser.quit()
