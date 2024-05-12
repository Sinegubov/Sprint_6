import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
from data import URL
from pages.base_page import BasePage
import allure
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderScooterLocators



class OrderPage(BasePage):

    def __init__(self, wd):
        super().__init__(wd)
        self.wd = wd

    def fill_order_form(self, first_name, surname, address, subway_station, mobile_number):
        self.find_page(OrderScooterLocators.first_name_field).send_keys(first_name)
        self.find_page(OrderScooterLocators.surname_field).send_keys(surname)
        self.find_page(OrderScooterLocators.address_field).send_keys(address)
        self.click_page(OrderScooterLocators.subway_station_field)
        self.find_page(OrderScooterLocators.subway_station_field).send_keys(subway_station)
        self.wait_until_element_is_visible(OrderScooterLocators.subway_station_choice)
        self.click_page(OrderScooterLocators.subway_station_choice)
        self.find_page(OrderScooterLocators.phone_field).send_keys(mobile_number)

    @allure.step('Нажать на кнопку Далее')
    def click_next_button(self):
        return self.click_page(BasePageLocators.next_button)

    @allure.step('Заполнение полей «Про аренду»')
    def fill_about_booking(self, comment):
        self.click_page(OrderScooterLocators.datepicker_field)
        self.click_page(OrderScooterLocators.datepicker)
        self.click_page(OrderScooterLocators.time_of_lease_field)
        self.click_page(OrderScooterLocators.time_of_lease_choice_one_day)
        self.click_page(OrderScooterLocators.color_grey_field)
        self.find_page(OrderScooterLocators.comment_field).send_keys(comment)

    @allure.step('Нажать кнопку Заказать')
    def click_finish_booking_button(self):
        return self.click_page(OrderScooterLocators.booking_button)

    @allure.step('Нажать кнопку "Вы уверены? - Да"')
    def click_are_you_sure_yes_button(self):
        return self.click_page(OrderScooterLocators.confidence_yes_button)

    @allure.step('Найти кнопку Посмотреть статус')
    def find_show_status_button(self):
        return self.find_page(OrderScooterLocators.show_status_button)

    def check_visible_success_message(self):
        pass

    def check_click_samokat_button(self):
        pass

    def check_click_yandex_logo(self):
        pass

