import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(ChromeDriverManager().install())
link = "http://suninjuly.github.io/cats.html"

try:

    # Open browser
    browser.get(link)

    # Wait for initialization for 5 sec
    browser.find_element(By.ID, "button")

finally:

    # Waiting 10 sec for see result
    time.sleep(10)
    # close browser
    browser.quit()
