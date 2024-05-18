# Sprint_6
Финальный проект 6 спринта
Автотесты для учебного сервиса «Яндекс. Самокат».

Проект состоит из файлов:

/pages - Для каждой страницы создан отдельный класс с Page Object.
/tests - Папка с тестовыми классами и методами содержащими UI-проверки. Для тестирования используется фреймворк pytest, 
используется параметризация входных данных 
conftest.py - Содержит фикстуры для запуска вебдрайвера
data.py - Файл со статичными данными для тестирования 
/locators - Сборник используемых локаторов с описанием Для запуска UI-тестов необходимо установить библиотеки:
/allure-results - папка для хранения отчета Allure

Установка необходимых модулей командой:

`pip3 install -r requirements.txt `

Запустить тесты из терминала можно командой:

`pytest -v --alluredir=allure_results `

Генерация отчета Allure командой:

`allure serve allure_results `


Тестирование на вебдрайвере Firefox


Тестовые сценарии
Выпадающий список в разделе «Вопросы о важном». Проверяется: когда нажимаешь на стрелочку, открывается соответствующий 
текст. Важно написать отдельный тест на каждый вопрос.

Заказ самоката. Проверяется весь флоу позитивного сценария с двумя наборами данных. 
Проверить точки входа в сценарий, их две: кнопка «Заказать» вверху страницы и внизу.

Позитивный сценарий состоит из:
- Нажать кнопку «Заказать». На странице две кнопки заказа.
- Заполнить форму заказа.
- Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа.
- Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».
- Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.