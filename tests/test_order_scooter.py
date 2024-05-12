import allure
import pytest
from data import URL
from pages.order_scooter_page import OrderPage
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderScooterLocators


class TestOrderScooter:

    def test_click_booking_header(self, wd):
        order_page = OrderPage(wd)
        order_page.open_base_url()
        order_page.click_order_button()
        order_page.wait_until_element_is_visible(BasePageLocators.next_button)

        assert order_page.show_current_url() == URL.ORDER_PAGE

    @pytest.mark.parametrize(
        "first_name, surname, address, subway_station, mobile_number, comment",
        [
            [
                "Джон",
                "Смит",
                "1-ая авеню 2",
                "Динамо",
                "+79996667788",
                "Тестовый комментарий",
            ],
            [
                "ПетрПервый",
                "Рюрикович",
                "Заячий остров 1",
                "Зорге",
                "+71112223344",
                "Текст",
            ],
        ],
    )
    def test_booking_form(self, wd, first_name, surname, address, subway_station, mobile_number, comment):
        booking_page = OrderPage(wd)
        booking_page.open_base_url()
        booking_page.click_order_button()
        booking_page.fill_order_form(first_name, surname, address, subway_station, mobile_number)
        booking_page.click_next_button()
        booking_page.fill_about_booking(comment)
        booking_page.click_finish_booking_button()
        booking_page.wait_until_element_is_clickable(OrderScooterLocators.confidence_yes_button)
        booking_page.click_are_you_sure_yes_button()
        assert booking_page.find_show_status_button().text == "Посмотреть статус"
