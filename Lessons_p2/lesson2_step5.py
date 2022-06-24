from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
link = "https://SunInJuly.github.io/execute_script.html"


try:

    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:

    # Waiting 10 sec for see result
    time.sleep(10)

    # close browser
    browser.quit()
