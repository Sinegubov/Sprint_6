import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import URL


class BasePage:

    def __init__(self, wd):
        self.wd = wd

    @allure.step("Открыть базовую страницу")
    def open_base_url(self):
        self.wd.get(URL.BASE_PAGE)

    @allure.step("Открыть страницу заказа самоката")
    def open_order_url(self):
        self.wd.get(URL.ORDER_PAGE)

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
        WebDriverWait(self.wd, 5).until(expected_conditions.presence_of_element_located(locator))

    @allure.step("Дождаться доступности кнопки для клика")
    def wait_until_button_is_clickable(self, locator):
        WebDriverWait(self.wd, 5).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step("Переключение на всплывающую вкладку")
    def switch_window(self):
        original_window = self.wd.current_window_handle
        for window_handle in self.wd.window_handles:
            if window_handle != original_window:
                self.wd.switch_to.window(window_handle)
                break

    @allure.step("Метод для прокрутки страницы вниз")
    def scroll_to_bottom_with_dynamic_loading(self):
        last_height = self.wd.execute_script("return document.body.scrollHeight")
        while True:
            self.wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            new_height = self.wd.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
