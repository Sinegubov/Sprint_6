import allure
import pytest
from data import URL, UserInfo
from pages.order_scooter_page import OrderPage
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderScooterLocators


class TestOrderScooter:

    @allure.title("Нажать кнопку «Заказать» (header)")
    @allure.description("Проверка открытия формы заказа по нажатию на кнопку «Заказать» в хэдере")
    def test_click_ordering_header(self, wd):
        order_page = OrderPage(wd)
        order_page.open_base_url()
        order_page.click_order_top_button()
        order_page.wait_until_element_is_visible(BasePageLocators.next_button)
        assert order_page.show_current_url() == URL.ORDER_PAGE

    @allure.title("Нажать кнопку «Заказать» (footer)")
    @allure.description("Проверка открытия формы заказа по нажатию на кнопку «Заказать» в футере")
    def test_click_ordering_footer(self, wd):
        order_page = OrderPage(wd)
        order_page.open_base_url()
        order_page.test_scroll_to_bottom_with_dynamic_loading(wd)
        order_page.click_order_bottom_button()
        order_page.wait_until_element_is_visible(BasePageLocators.next_button)
        assert order_page.show_current_url() == URL.ORDER_PAGE

    @allure.title("Заполнение формы оформления заказа (positive case)")
    @allure.description("Проверка создания заказа при вводе двух наборов данных в форме оформления заказа")
    @pytest.mark.parametrize(
        "first_name, surname, address, subway_station, mobile_number, comment",
        [
            [
                UserInfo.first_name[0], UserInfo.surname[0], UserInfo.address[0], UserInfo.subway_station[0],
                UserInfo.mobile_number[0], UserInfo.comment[0]
            ],
            [
                UserInfo.first_name[1], UserInfo.surname[1], UserInfo.address[1], UserInfo.subway_station[1],
                UserInfo.mobile_number[1], UserInfo.comment[1]
            ],
        ],
    )
    def test_ordering_form(self, wd, first_name, surname, address, subway_station, mobile_number, comment):
        order_page = OrderPage(wd)
        order_page.open_base_url()
        order_page.click_order_top_button()
        order_page.fill_order_form(first_name, surname, address, subway_station, mobile_number)
        order_page.click_next_button()
        order_page.fill_about_ordering(comment)
        order_page.click_finish_ordering_button()
        order_page.wait_until_element_is_clickable(OrderScooterLocators.confidence_yes_button)
        order_page.click_are_you_sure_yes_button()
        assert order_page.check_visible_success_message().text == "Посмотреть статус"

    @allure.title("Нажать на логотип «Самоката»")
    @allure.description("Проверка, если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»")
    def test_redirect_scooter(self, wd):
        redirect_page = OrderPage(wd)
        redirect_page.open_base_url()
        redirect_page.click_order_top_button()
        redirect_page.click_scooter_button()
        redirect_page.wait_until_element_is_visible(BasePageLocators.order_btn_bottom)
        assert redirect_page.show_current_url() == URL.BASE_PAGE

    @allure.title("Нажать на логотип Яндекса")
    @allure.description("Проверка, если нажать на лого Яндекса, "
                        "в новом окне через редирект откроется главная страница «Дзена»")
    def test_redirect_dzen(self, wd):
        redirect_page = OrderPage(wd)
        redirect_page.open_base_url()
        redirect_page.click_order_top_button()
        assert len(wd.window_handles) == 1
        redirect_page.click_yandex_logo()
        redirect_page.switch_window()
        redirect_page.wait_until_element_is_clickable(BasePageLocators.dzen_main)
        assert redirect_page.show_current_url() == URL.DZEN_PAGE
