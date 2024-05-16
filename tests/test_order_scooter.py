import allure
import pytest
from data import URL, UserInfo
from pages.order_scooter_page import OrderPage
from pages.main_page import MainPage


class TestOrderScooter:

    @allure.title("Нажать кнопку «Заказать» (header)")
    @allure.description("Проверка открытия формы заказа по нажатию на кнопку «Заказать» в хэдере")
    def test_click_ordering_header(self, wd):
        order_page = OrderPage(wd)
        order_page.open_base_url()
        main_page = MainPage(wd)
        main_page.click_cookies_yes_button()
        order_page.click_order_top_button()
        order_page.wait_until_next_button_is_clickable()
        assert order_page.show_current_url() == URL.ORDER_PAGE

    @allure.title("Нажать кнопку «Заказать» (footer)")
    @allure.description("Проверка открытия формы заказа по нажатию на кнопку «Заказать» в футере")
    def test_click_ordering_footer(self, wd):
        order_page = OrderPage(wd)
        order_page.open_base_url()
        main_page = MainPage(wd)
        main_page.click_cookies_yes_button()
        main_page.scroll_to_bottom_with_dynamic_loading()
        order_page.wait_until_order_btn_bottom_is_visible()
        order_page.click_order_bottom_button()
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
        main_page = MainPage(wd)
        main_page.click_cookies_yes_button()
        order_page.click_order_top_button()
        order_page.fill_order_form(first_name, surname, address, subway_station, mobile_number)
        order_page.wait_until_order_second_form_is_visible()
        order_page.fill_about_ordering(comment)
        assert order_page.check_visible_success_message() == "Посмотреть статус"

    @allure.title("Нажать на логотип «Самоката»")
    @allure.description("Проверка, если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»")
    def test_redirect_scooter(self, wd):
        redirect_page = MainPage(wd)
        redirect_page.open_order_url()
        redirect_page.click_scooter_button()
        assert redirect_page.show_current_url() == URL.BASE_PAGE

    @allure.title("Нажать на логотип Яндекса")
    @allure.description("Проверка, если нажать на лого Яндекса, "
                        "в новом окне через редирект откроется главная страница «Дзена»")
    def test_redirect_dzen(self, wd):
        redirect_page = OrderPage(wd)
        redirect_page.open_base_url()
        redirect_page.click_order_top_button()
        assert len(wd.window_handles) == 1
        main_page = MainPage(wd)
        main_page.click_yandex_logo()
        main_page.switch_window()
        main_page.wait_until_dzen_is_visible()
        assert redirect_page.show_current_url() == URL.DZEN_PAGE
