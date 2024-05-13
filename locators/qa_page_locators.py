from selenium.webdriver.common.by import By


class QAPageLocators:
    question_zero = [By.XPATH, '//div[@class="accordion__button"]']  # Вопросы
    question_one = [By.XPATH, '(//div[@class="accordion__button"])[2]']  # Вопросы
    question_two = [By.XPATH, '(//div[@class="accordion__button"])[3]']  # Вопросы
    question_three = [By.XPATH, '(//div[@class="accordion__button"])[4]']  # Вопросы
    question_four = [By.XPATH, '(//div[@class="accordion__button"])[5]']  # Вопросы
    question_five = [By.XPATH, '(//div[@class="accordion__button"])[6]']  # Вопросы
    question_six = [By.XPATH, '(//div[@class="accordion__button"])[7]']  # Вопросы
    question_seven = [By.XPATH, '(//div[@class="accordion__button"])[8]']  # Вопросы
    answer_zero = [By.XPATH, "//p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']"]  # Ответы
    answer_one = [By.XPATH, "//p[text()='Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']"]  # Ответы
    answer_two = [By.XPATH, "//p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']"]  # Ответы
    answer_three = [By.XPATH, "//p[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']"]  # Ответы
    answer_four = [By.XPATH, "//p[text()='Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']"]  # Ответы
    answer_five = [By.XPATH, "//p[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']"]  # Ответы
    answer_six = [By.XPATH, "//p[text()='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']"]  # Ответы
    answer_seven = [By.XPATH, "//p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']"]  # Ответы
