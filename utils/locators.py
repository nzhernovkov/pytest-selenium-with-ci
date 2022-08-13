from selenium.webdriver.common.by import By


class BasePageLocators:
    DESKTOP_LOGO = (By.CSS_SELECTOR, "#headerDesktopHiddenPart > .header__logo")


class MainPageLocators:
    FIND_OFFICE_LINK = (By.CSS_SELECTOR, '.form-bar-desktop [href*=find_an_office]')


class OfficePageLocators:
    MAP_CONTAINER = (By.CSS_SELECTOR, '.map__container')
