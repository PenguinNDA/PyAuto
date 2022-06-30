from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
import time

# Open Firefox
browser_ff = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser_ff.get("https://stepik.org/lesson/25969/step/8")

# Wait for result
time.sleep(10)

# Close browser
browser_ff.quit()
