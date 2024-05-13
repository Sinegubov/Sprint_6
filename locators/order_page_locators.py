from selenium.webdriver.common.by import By


class OrderScooterLocators:
    header_ord_frm = [By.CLASS_NAME, 'Order_Header__BZXOb']  # Заголовок "Для кого самокат"
    header_booking_button = (By.XPATH, './/button[@class="Button_Button__ra12g" and text() = "Заказать"]')
    first_name = (By.XPATH, './/input[@placeholder="* Имя"]')  # Имя
    surname = (By.XPATH, './/input[@placeholder="* Фамилия"]')  # Фамилия
    address = (By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]')  # Адрес
    subway_station_field = (By.XPATH, './/input[@placeholder="* Станция метро"]')  # Станция метро
    subway_station_choice = (By.XPATH, './/div[@class="select-search__select"]')   # Станция метро выбор
    phone = (By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]')  # Телефон
    datepicker_field = (By.XPATH, './/input[@placeholder="* Когда привезти самокат"]')  # Когда привезти самокат
    datepicker = (
        By.XPATH,
        '//div[@class="react-datepicker__day react-datepicker__day--031"]'
    )  # Когда привезти самокат 31 мая
    time_of_lease = (By.XPATH, './/div[@class="Dropdown-placeholder" and text() = "* Срок аренды"]')  # Срок аренды
    time_of_lease_choice_one_day = (By.XPATH, './/div[text() = "сутки"]')  # Срок аренды Сутки
    color_grey = (By.XPATH, './/label[text() = "серая безысходность"]')  # Цвет самоката Серый
    comment = (By.XPATH, './/input[@placeholder="Комментарий для курьера"]')  # Комментарий для курьера
    booking_button = (
        By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text() = "Заказать"]'
    )  # Нажать кнопку Заказать
    confidence_yes_button = (By.XPATH, './/button[text() = "Да"]')  # Нажать кнопку "Хотите оформить заказ? - Да
    show_status_button = (
        By.XPATH,
        './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text() = "Посмотреть статус"]'
    )  # Посмотреть статус
