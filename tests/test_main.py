from page_objects.MainPage import MainPage
import allure
import time 

url = "https://demo-opencart.ru/"

@allure.suite("Главная страница")
@allure.title("Проверка отображения элементов")
def test_check_main(browser):
    browser.get(url)
    MainPage(browser).check_title()
    MainPage(browser).check_search()
    MainPage(browser).check_h3()
    MainPage(browser).check_button()
    MainPage(browser).check_click_button()
    

@allure.suite("Главная страница")
@allure.title("Проверка поиска на главной странице")
def test_main_search(browser):
    browser.get(url)
    MainPage(browser).check_title()
    MainPage(browser).input_search("iphone")
    MainPage(browser).click_search()
    time.sleep(60)
    MainPage(browser).check_count_product_1()
    

@allure.suite("Главная страница")
@allure.title("Проверка отображения раздела Рекомендуемые")
def test_main_req(browser):
    browser.get(url)
    MainPage(browser).check_h3()
    MainPage(browser).check_count_product_4()
    
