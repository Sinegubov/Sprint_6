from selenium.webdriver.common.by import By


class BasePageLocators:
    order_btn_top = [By.XPATH, '(//button[text()="Заказать"])[1]']  # Кнопка "Заказать" сверху страницы
    order_btn_bottom = [By.XPATH, '(//button[text()="Заказать"])[2]']  # Кнопка "Заказать" снизу страницы
    next_button = (By.XPATH, './/button[text() = "Далее"]')  # Кнопка "Далее"
    cookies_yes_button = (
        By.XPATH, './/button[@class="App_CookieButton__3cvqF" and text() = "да все привыкли"]'
    )  # Кнопка согласия с куками
    yandex_logo = (By.XPATH, '//img[@alt="Yandex"]')  # Логотип Яндекса
    dzen_main = (By.XPATH, '//a[@href="/"]//li[1]')  # Раздел Главное страницы Дзен
    scooter_btn = (By.XPATH, '//img[@alt="Scooter"]')  # Логотип Самоката
