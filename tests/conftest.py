import pytest
from selenium import webdriver
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    # ------Path to executable chrome driver ---------
    exec_path = r"C:\\chromedriver.exe"
    driver: WebDriver = webdriver.Chrome(executable_path=exec_path)
    driver.get("https://graph.facebook.com/1234567/feed")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
