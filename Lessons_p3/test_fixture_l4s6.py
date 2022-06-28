import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(ChromeDriverManager().install())
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(autouse=True)  # When we use "autouse = true", we will use it in any case
def prepare_data():
    print()
    print("preparing some critical data for every test")


class TestMainPage1:

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
