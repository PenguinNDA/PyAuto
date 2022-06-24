from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# Create our variable
link = "https://www.google.com/"
browser = webdriver.Chrome(ChromeDriverManager().install())


try:

    # Open browser
    browser.get(link)

    # Use execute_script
    browser.execute_script("document.title='Script executing';alert('Robots at work');")

finally:

    # Waiting 10 sec for see result
    time.sleep(10)

    # close browser
    browser.quit()
