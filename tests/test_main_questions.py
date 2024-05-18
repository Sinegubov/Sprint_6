import allure
import pytest
from data import QAInfo
from pages.main_page import MainPage
from locators.qa_page_locators import QAPageLocators


class TestMainQuestions:
    @allure.title("Открыть раздел «Вопросы о важном»")
    @allure.description("Проверка, когда нажимаешь на стрелочку, открывается соответствующий текст")
    @pytest.mark.parametrize("quest, answ, answers",
                             [
                                 [QAPageLocators.question_zero, QAPageLocators.answer_zero, QAInfo.answers[0]],
                                 [QAPageLocators.question_one, QAPageLocators.answer_one, QAInfo.answers[1]],
                                 [QAPageLocators.question_two, QAPageLocators.answer_two, QAInfo.answers[2]],
                                 [QAPageLocators.question_three, QAPageLocators.answer_three, QAInfo.answers[3]],
                                 [QAPageLocators.question_four, QAPageLocators.answer_four, QAInfo.answers[4]],
                                 [QAPageLocators.question_five, QAPageLocators.answer_five, QAInfo.answers[5]],
                                 [QAPageLocators.question_six, QAPageLocators.answer_six, QAInfo.answers[6]],
                                 [QAPageLocators.question_seven, QAPageLocators.answer_seven, QAInfo.answers[7]],
                             ],
                             )
    def test_check_answers(self, wd, quest, answ, answers):
        qa_page = MainPage(wd)
        qa_page.open_base_url()
        qa_page.click_cookies_yes_button()
        qa_page.click_dropdown_menu_button(quest)
        qa_page.wait_until_element_is_visible(answ)
        assert qa_page.find_page(answ).text == answers
