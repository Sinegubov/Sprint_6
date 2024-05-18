class URL:
    BASE_PAGE = 'https://qa-scooter.praktikum-services.ru/'
    ORDER_PAGE = f"{BASE_PAGE}order"
    DZEN_PAGE = "https://dzen.ru/?yredirect=true&is_autologin_ya=true"


class UserInfo:
    first_name = ('Джон', 'ПетрПервый')
    surname = ('Смит', 'Рюрикович')
    address = ('1-ая авеню 2', 'Заячий остров 1')
    subway_station = ('Динамо', 'Зорге')
    mobile_number = ('+79996667788', '+71112223344')
    comment = ('Тестовый комментарий', 'Текст')


class QAInfo:
    answers = [
        "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
    ]
    