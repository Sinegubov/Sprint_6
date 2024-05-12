from selenium.webdriver.common.by import By


class BasePageLocators:
    order_btn = [By.XPATH, '//button[text()="Заказать"]']  # Кнопка "Заказать"
    next_button = (By.XPATH, './/button[text() = "Далее"]')
    cookies_yes_button = (By.XPATH, './/button[@class="App_CookieButton__3cvqF" and text() = "да все привыкли"]')
