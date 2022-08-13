# Pytest Selenium with CI

## О проекте

Проект для выполнения тестового задания.

### Требования

- Python 3.7+
- [Chromedriver](https://chromedriver.chromium.org/)
- [Allure](https://docs.qameta.io/allure/#_installing_a_commandline)

### Запуск

1. Клонировать репозиторий - `git clone https://github.com/nzhernovkov/pytest_allure_test_project.git`
2. Установить зависимости - `pip install -r requirements.txt`
3. Запустить тесты:

- локально - `pytest --alluredir=./allure_results`
- на удаленном сервере - `pytest --alluredir=./allure_results --selenium_host=127.0.0.1 --selenium_port=4444`

4. Сгенерировать Allure отчет - `allure serve ./allure_results`