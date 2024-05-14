import allure
from pages.main_page import MainPage
from locators.order_page_locators import OrderScooterLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class OrderPage(MainPage):

    def __init__(self, wd):
        super().__init__(wd)
        self.wd = wd

    @allure.step("Дождаться, чтобы на элемент Далее можно было нажать")
    def wait_until_next_button_is_clickable(self):
        return WebDriverWait(self.wd, 5).until(
            expected_conditions.element_to_be_clickable(OrderScooterLocators.next_button)
        )

    @allure.step("Дождаться загрузки кнопки заказать внизу страницы")
    def wait_until_order_btn_bottom_is_visible(self):
        return WebDriverWait(self.wd, 5).until(
            expected_conditions.presence_of_element_located(OrderScooterLocators.order_btn_bottom)
        )

    @allure.step("Кликаем кнопку 'Заказать' в хэдере")
    def click_order_top_button(self):
        self.click_page(OrderScooterLocators.order_btn_top)

    @allure.step("Кликаем кнопку 'Заказать' в футере")
    def click_order_bottom_button(self):
        self.click_page(OrderScooterLocators.order_btn_bottom)

    @allure.step("Дождаться загрузки второй формы оформления заказа")
    def wait_until_order_second_form_is_visible(self):
        return WebDriverWait(self.wd, 5).until(
            expected_conditions.presence_of_element_located(OrderScooterLocators.header_ord_frm_2)
        )

    @allure.step('Заполнение полей «Для кого самокат»')
    def fill_order_form(self, first_name, surname, address, subway_station, mobile_number):
        self.find_page(OrderScooterLocators.first_name).send_keys(first_name)
        self.find_page(OrderScooterLocators.surname).send_keys(surname)
        self.find_page(OrderScooterLocators.address).send_keys(address)
        self.click_page(OrderScooterLocators.subway_station_field)
        self.find_page(OrderScooterLocators.subway_station_field).send_keys(subway_station)
        self.wait_until_element_is_visible(OrderScooterLocators.subway_station_choice)
        self.click_page(OrderScooterLocators.subway_station_choice)
        self.find_page(OrderScooterLocators.phone).send_keys(mobile_number)
        self.click_page(OrderScooterLocators.next_button)

    @allure.step('Заполнение полей «Про аренду»')
    def fill_about_ordering(self, comment):
        self.click_page(OrderScooterLocators.datepicker_field)
        self.click_page(OrderScooterLocators.datepicker)
        self.click_page(OrderScooterLocators.time_of_lease)
        self.click_page(OrderScooterLocators.time_of_lease_choice_one_day)
        self.click_page(OrderScooterLocators.color_grey)
        self.find_page(OrderScooterLocators.comment).send_keys(comment)
        self.click_page(OrderScooterLocators.booking_button)
        self.click_page(OrderScooterLocators.confidence_yes_button)

    @allure.step('Найти кнопку Посмотреть статус')
    def check_visible_success_message(self):
        return self.find_page(OrderScooterLocators.show_status_button).text
