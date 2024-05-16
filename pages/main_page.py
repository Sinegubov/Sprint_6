import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Дождаться загрузки меню на странице Дзен")
    def wait_until_dzen_is_visible(self):
        self.wait_until_element_is_visible(MainPageLocators.dzen_main)

    @allure.step("Принять cookies")
    def click_cookies_yes_button(self):
        self.click_page(MainPageLocators.cookies_yes_button)

    @allure.step("Нажать на стрелочку у вопроса из списка")
    def click_dropdown_menu_button(self, *locator):
        self.click_page(*locator)

    @allure.step('Нажатие на логотип «Самоката»')
    def click_scooter_button(self):
        self.click_page(MainPageLocators.scooter_btn)

    @allure.step('Нажатие на логотип Яндекса')
    def click_yandex_logo(self):
        self.click_page(MainPageLocators.yandex_logo)
