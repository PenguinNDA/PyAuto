from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(ChromeDriverManager().install())
link = "http://suninjuly.github.io/simple_form_find_task.html"

try:

    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # Close browser after all manipulation
    browser.quit()
