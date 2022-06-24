import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as exp_con
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(ChromeDriverManager().install())
link = "http://suninjuly.github.io/explicit_wait2.html"


# Some math tricks
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    # Open browser
    browser.get(link)

    # Wait for initialization for 5 sec
    browser.implicitly_wait(5)

    # Find button with price
    bookButton = browser.find_element(By.ID, "book")

    # Wait for 100$
    priceField = WebDriverWait(browser, 15).until(
        exp_con.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Click to button
    bookButton.click()

    # Find number
    number = int(browser.find_element(By.ID, "input_value").text)

    # Use math tricks
    answer = calc(number)

    # Input in text field
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(answer)

    # Find second button and press
    buttonAnswer = browser.find_element(By.ID, "solve")
    buttonAnswer.click()

finally:

    # Waiting 10 sec for see result
    time.sleep(10)
    # close browser
    browser.quit()
