from selenium import webdriver
import pytest


@pytest.fixture
def wd():
    wd = webdriver.Firefox()
    yield wd
    wd.quit()


# Корректное отображение юникода в параметризованных тестах
def pytest_make_parametrize_id(config, val):
    return repr(val)
