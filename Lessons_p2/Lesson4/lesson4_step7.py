import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as exp_con
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(ChromeDriverManager().install())
link = "http://suninjuly.github.io/wait2.html"

try:

    # Open browser
    browser.get(link)

    # Wait for initialization for 5 sec
    browser.implicitly_wait(5)

    # Click to button
    button = WebDriverWait(browser, 5).until(
        exp_con.element_to_be_clickable((By.ID, "verify"))
    )
    button.click()

    # Find our text
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:

    # Waiting 10 sec for see result
    time.sleep(10)
    # close browser
    browser.quit()
