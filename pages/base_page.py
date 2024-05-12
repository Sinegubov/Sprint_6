import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
from data import URL


class BasePage:

    def __init__(self, wd):
        self.wd = wd

    @allure.step("Открыть стартовую страницу")
    def open_base_url(self):
        return self.wd.get(URL.BASE_PAGE)

    @allure.step("Кликаем кнопку 'Заказать' в хэдере")
    def click_order_button(self):
        return self.wd.find_element(*BasePageLocators.order_btn).click()

    @allure.step("Вернуть адрес текущей страницы")
    def show_current_url(self):
        return self.wd.current_url

    @allure.step("Найти страницу или элемент")
    def find_page(self, locator):
        return self.wd.find_element(*locator)

    @allure.step("Нажать на страницу или элемент")
    def click_page(self, locator):
        self.wd.find_element(*locator).click()

    @allure.step("Дождаться загрузки элемента")
    def wait_until_element_is_visible(self, locator):
        return WebDriverWait(self.wd, 5).until(
            expected_conditions.presence_of_element_located(locator)
        )

    @allure.step("Дождаться, чтобы на элемент можно было нажать")
    def wait_until_element_is_clickable(self, locator):
        return WebDriverWait(self.wd, 5).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    def click_cookies_yes_button(self):
        return self.click_page(BasePageLocators.cookies_yes_button)