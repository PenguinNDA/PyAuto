from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Create our variable
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome(ChromeDriverManager().install())


try:

    # Open browser
    browser.get(link)

    # Find sum
    first_number = int(browser.find_element(By.ID, 'num1').text)
    second_number = int(browser.find_element(By.ID, 'num2').text)
    sum = first_number + second_number

    # Select 'sum' from list
    list_of_values = Select(browser.find_element(By.TAG_NAME, "select"))
    list_of_values.select_by_visible_text(str(sum))

    # press button "Submit"
    submit_button = browser.find_element(By.TAG_NAME, "button")
    submit_button.click()

finally:

    # Waiting 10 sec for see result
    time.sleep(10)

    # close browser
    browser.quit()
