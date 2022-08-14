import allure

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.locators import BasePageLocators
from utils.selenium_confs import IMPLICITLY_TIMEOUT, WAIT_FOR_TIMEOUT


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(IMPLICITLY_TIMEOUT)

    @allure.step('Открыть страницу по ссылке {url}')
    def open(self, url):
        self.browser.get(url)
        return self

    @allure.step('Проверить, что страница загружена')
    def is_page_loaded(self):
        assert self.is_element_present(*BasePageLocators.DESKTOP_LOGO), \
            'Лого "Boxberry" не отобразилось на странице, вероятно, страница не загружена'
        return self

    @allure.step('Проверить, что текст {text} отображается на странице')
    def is_text_visible(self, text):
        xpath_string = xpath_prepare(text)
        try:
            WebDriverWait(self.browser, WAIT_FOR_TIMEOUT).until(
                EC.visibility_of_element_located((By.XPATH, xpath_string))
            )
        except TimeoutException:
            return False
        return True

    @allure.step('Проверить, что элемент с селектором {what} присутствует на странице')
    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, WAIT_FOR_TIMEOUT).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    @allure.step('Проверить, что элемент с селектором {what} отсутствует на странице')
    def is_not_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, WAIT_FOR_TIMEOUT).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True
        return False


def xpath_prepare(search_text):
    """
    Вспомогательная функция для поиска текста на странице без учета регистра
    @return: xpath string
    """
    return ".//*[contains(translate(., '$u', '$l'), '$s')]".replace("$u", search_text.upper()) \
        .replace("$l", search_text.lower()) \
        .replace("$s", search_text.lower())
