from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
link = "http://suninjuly.github.io/file_input.html"


try:

    # Open browser
    browser.get(link)

    # input our data
    input_first_name = browser.find_element(By.CSS_SELECTOR, '.form-control:first-of-type')
    input_first_name.send_keys('Misha')

    input_second_name = browser.find_element(By.CSS_SELECTOR, '.form-control:nth-of-type(2)')
    input_second_name.send_keys('Vazovski')

    input_mail = browser.find_element(By.CSS_SELECTOR, '.form-control:last-of-type')
    input_mail.send_keys('sens@qa.qa')

    # Find path for txt file
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'clear file.txt')

    # send file to server
    send_file = browser.find_element(By.ID, 'file')
    send_file.send_keys(file_path)

    # Click to button
    submit_button = browser.find_element(By.TAG_NAME, 'button')
    submit_button.click()

finally:

    # Waiting 10 sec for see result
    time.sleep(10)

    # close browser
    browser.quit()
