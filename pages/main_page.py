import allure
#
# from locators.base_page_locators import BasePageLocators
# from locators.order_page_locators import OrderScooterLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Открыть страницу (URL)')
    def get_url(self, url):
        self.wd.get(url)
