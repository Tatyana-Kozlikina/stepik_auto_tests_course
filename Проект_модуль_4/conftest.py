import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en, es...")

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart")
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages':language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(30)

    yield browser
    print("\nquit")
    time.sleep(15)
    browser.quit()
