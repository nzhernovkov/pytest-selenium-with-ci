import allure

from utils.environment import OFFICE_PAGE
from utils.locators import OfficePageLocators
from .base_page import BasePage


class OfficePage(BasePage):
    @allure.step('Открыть страницу "Наши отделения" по ссылке {url}')
    def open_this_page(self, url=OFFICE_PAGE):
        self.browser.get(url)
        return self

    @allure.step('Проверить, что открыта страница "Наши отделения"')
    def is_office_page_opened(self):
        assert self.is_element_present(*OfficePageLocators.MAP_CONTAINER), 'Контейнер с картой не отобразился на странице'
        assert self.is_text_visible('Найти отделение'), 'Текст "Найти отделение" не отобразился на странице'
        assert self.is_text_visible('Открыть в Яндекс.Картах'), 'Текст "Открыть в Яндекс.Картах" не отобразился на странице'
