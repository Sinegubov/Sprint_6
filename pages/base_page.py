import allure
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
from data import URL


class BasePage:

    def __init__(self, wd):
        self.wd = wd

    @allure.step("Открыть базовую страницу")
    def open_base_url(self):
        return self.wd.get(URL.BASE_PAGE)

    @allure.step("Кликаем кнопку 'Заказать' в хэдере")
    def click_order_top_button(self):
        return self.wd.find_element(*BasePageLocators.order_btn_top).click()

    @allure.step("Кликаем кнопку 'Заказать' в футере")
    def click_order_bottom_button(self):
        return self.wd.find_element(*BasePageLocators.order_btn_bottom).click()

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

    @allure.step("Принять cookies")
    def click_cookies_yes_button(self):
        return self.click_page(BasePageLocators.cookies_yes_button)

    @staticmethod
    @allure.step("Статичный метод для прокрутки страницы вниз")
    def test_scroll_to_bottom_with_dynamic_loading(wd):
        last_height = wd.execute_script("return document.body.scrollHeight")
        while True:
            wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Ждем некоторое время для загрузки контента
            new_height = wd.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    @allure.step("Переключение на всплывающую вкладку")
    def switch_window(self):
        original_window = self.wd.current_window_handle
        for window_handle in self.wd.window_handles:
            if window_handle != original_window:
                self.wd.switch_to.window(window_handle)
                break

    @allure.step("Нажать на стрелочку у вопроса из списка")
    def click_dropdown_menu_button(self, *locator):
        return self.click_page(*locator)
