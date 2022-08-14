import allure
import pytest

from pages.main_page import MainPage
from pages.ofiice_page import OfficePage


@allure.suite('Тесты для главной страницы')
@pytest.mark.main_page
class TestOfficePage:
    @allure.title('Проверка работы ссылки "Наши отделения"')
    def test_find_an_office_link(self, browser):
        page = MainPage(browser)
        page.open_this_page().is_page_loaded() \
            .click_find_office_link()
        page = OfficePage(browser)
        page.is_office_page_opened()
