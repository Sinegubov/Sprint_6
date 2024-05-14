import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, wd):
        super().__init__(wd)
        self.wd = wd

    @allure.step("Дождаться загрузки меню на странице Дзен")
    def wait_until_dzen_is_visible(self):
        return WebDriverWait(self.wd, 5).until(
            expected_conditions.presence_of_element_located(MainPageLocators.dzen_main)
        )

    @allure.step("Принять cookies")
    def click_cookies_yes_button(self):
        return self.click_page(MainPageLocators.cookies_yes_button)

    @staticmethod
    @allure.step("Статичный метод для прокрутки страницы вниз")
    def scroll_to_bottom_with_dynamic_loading(wd):
        last_height = wd.execute_script("return document.body.scrollHeight")
        while True:
            wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            WebDriverWait(wd, 10).until(
                expected_conditions.presence_of_element_located(MainPageLocators.questions_field))
            new_height = wd.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    @allure.step("Нажать на стрелочку у вопроса из списка")
    def click_dropdown_menu_button(self, *locator):
        return self.click_page(*locator)

    @allure.step('Нажатие на логотип «Самоката»')
    def click_scooter_button(self):
        return self.click_page(MainPageLocators.scooter_btn)

    @allure.step('Нажатие на логотип Яндекса')
    def click_yandex_logo(self):
        return self.click_page(MainPageLocators.yandex_logo)
