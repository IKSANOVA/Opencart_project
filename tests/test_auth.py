from page_objects.AuthPage import AuthPage
import allure
import pytest


url = "https://demo-opencart.ru/index.php?route=account/login"


@allure.suite("Страница авторизации")
@allure.title("Проверка отображения элементов")
def test_check_register(browser):
    browser.get(url)
    AuthPage(browser).check_email()
    AuthPage(browser).check_password()
    AuthPage(browser).check_button_submit()
    

@allure.suite("Страница авторизации")
@allure.title("Успешная авторизация") 
def test_register_success(browser):
    browser.get(url)
    AuthPage(browser).input_email("limma@yandex.ru")
    AuthPage(browser).input_password("Tester")
    AuthPage(browser).click_button_submit()
    AuthPage(browser).check_success()
    
@allure.suite("Страница авторизации")
@allure.title("Неуспешная авторизация") 
@pytest.mark.parametrize('email', ['test1', 'test_00', '@'])
@pytest.mark.parametrize('password', ['test1', 'test_00', '_11'])
def test_register_no_success(browser, email, password):
    browser.get(url)
    AuthPage(browser).input_email(email)
    AuthPage(browser).input_password(password)
    AuthPage(browser).click_button_submit()
    AuthPage(browser).check_no_success()

