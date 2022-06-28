import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import math


# Some math magic
def answer(x):
    return math.log(int(x))


# Open and close browser
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(ChromeDriverManager().install())
    yield browser
    print("\nquit browser..")
    browser.quit()


# New class for test
class TestMainPage1:

    # Use parametrize for get all links
    @pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_lesson6_step3(self, browser, link):

        link = f"https://stepik.org/lesson/{link}/step/1"

        # Open browser and wait for page will be open
        browser.get(link)
        browser.implicitly_wait(10)

        # Take current time...
        x = time.time()

        # For some magic trick here
        browser.find_element(By.CSS_SELECTOR, ".textarea").send_keys(str(answer(x)))

        # Click to button and wait for result
        browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
        result = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
        assert result == "Correct!", f"Get '{result}' instead of 'Correct!'"
