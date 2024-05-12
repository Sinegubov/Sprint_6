from selenium import webdriver
import pytest


@pytest.fixture
def wd():
    wd = webdriver.Firefox()
    yield wd
    wd.quit()
