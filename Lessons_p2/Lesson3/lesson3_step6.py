from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
link = "http://suninjuly.github.io/redirect_accept.html"


# Some math tricks
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    # Open browser
    browser.get(link)

    # Find button and click it
    button_redirect = browser.find_element(By.TAG_NAME, 'button')
    button_redirect.click()

    # Switch to new window
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Find number
    math_x = browser.find_element(By.ID, 'input_value').text

    # Use math tricks
    math_y = calc(int(math_x))

    # Input our data to text fields
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(math_y)

    # Find button and click it
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:

    # Waiting 10 sec for see result
    time.sleep(10)

    # close browser
    browser.quit()
