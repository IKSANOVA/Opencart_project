from page_objects.RegisterPage import RegisterPage
from faker import Faker
import allure

fake = Faker("ru_RU")

url = "https://demo-opencart.ru/index.php?route=account/register"
name = fake.first_name()
surname = fake.last_name()
telephon = fake.phone_number()
email = fake.email()
passw = "qwerty123"


@allure.suite("Страница регистрации")
@allure.title("Проверка отображения элементов")
def test_check_register(browser):
    browser.get(url)
    RegisterPage(browser).check_firstname()
    RegisterPage(browser).check_lastname()
    RegisterPage(browser).check_email()
    RegisterPage(browser).check_telephon()
    
    
@allure.suite("Страница регистрации")
@allure.title("Регистрация")
def test_register(browser):    
    browser.get(url)
    RegisterPage(browser).input_firstname(name)
    RegisterPage(browser).input_lastname(surname)
    RegisterPage(browser).input_email(email)
    RegisterPage(browser).input_telephon(telephon)
    RegisterPage(browser).input_passw(passw)
    RegisterPage(browser).input_conf_passw(passw)
    RegisterPage(browser).click_agree()
    RegisterPage(browser).click_button_next()
    RegisterPage(browser).check_reg_successfully()
