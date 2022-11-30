import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def chrome_browser_instance(request):
    """
    Provide a selenium webdrive instance
    """
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.close()
