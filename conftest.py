import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from allure_commons.types import AttachmentType

from utils.selenium_confs import PAGE_LOAD_TIMEOUT


def pytest_addoption(parser):
    parser.addoption('--selenium_host', action='store', default=None,
                     help="Set selenium host address")
    parser.addoption('--selenium_port', action='store', default='4444',
                     help="Set selenium host port")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def driver(request):
    selenium_host = request.config.getoption("selenium_host")
    selenium_port = request.config.getoption("selenium_port")
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("window-size=1920x1080")
    if selenium_host:
        driver = webdriver.Remote(
            command_executor=f'http://{selenium_host}:{selenium_port}/wd/hub',
            options=chrome_options
        )
        print(f"\nstart chrome browser on remote selenium host - {selenium_host}:{selenium_port}")
    else:
        driver = webdriver.Chrome(options=chrome_options)
        print("\nstart chrome browser")
    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
    driver.maximize_window()
    return driver


@pytest.fixture(scope="function")
def browser(request, driver):
    yield driver
    # Make screenshot if test fails
    if request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name=request.function.__name__,
            attachment_type=AttachmentType.PNG
        )
    print("\nquit browser..")
    driver.quit()
