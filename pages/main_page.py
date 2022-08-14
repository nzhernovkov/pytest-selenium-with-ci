import allure

from utils.environment import MAIN_PAGE
from utils.locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    @allure.step('Открыть главную страницу по ссылке {url}')
    def open_this_page(self, url=MAIN_PAGE):
        self.browser.get(url)
        return self

    @allure.step('Нажать на ссылку "Наши отделения"')
    def click_find_office_link(self):
        link = self.browser.find_element(*MainPageLocators.FIND_OFFICE_LINK)
        link.click()
        return self
