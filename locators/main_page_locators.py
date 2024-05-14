from selenium.webdriver.common.by import By


class MainPageLocators:
    cookies_yes_button = (
        By.XPATH, './/button[@class="App_CookieButton__3cvqF" and text() = "да все привыкли"]'
    )  # Кнопка согласия с куками
    yandex_logo = (By.XPATH, '//img[@alt="Yandex"]')  # Логотип Яндекса
    dzen_main = (By.XPATH, '//a[@href="/"]//li[1]')  # Раздел Главное страницы Дзен
    scooter_btn = (By.XPATH, '//img[@alt="Scooter"]')  # Логотип Самоката
    questions_field = (By.XPATH, "//div[text()='Вопросы о важном']")  # Футер
