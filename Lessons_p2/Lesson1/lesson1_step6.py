from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Create our variable
link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome(ChromeDriverManager().install())


try:

    browser.get(link)

# Check peopleRule for attribute 'Checked'
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

# Check robotRule for attribute 'Checked'
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots_radio: ", robots_checked)
    assert robots_checked is None

# Check button for attribute 'disabled'
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit: ", button_disabled)
    assert button_disabled is None

# Check button for attribute 'disabled' after 10 seconds sleep
    time.sleep(10)
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit after 10sec: ", button_disabled)
    assert button_disabled is not None

finally:

    # Waiting 10 sec for see result
    time.sleep(10)

    # close browser
    browser.quit()
