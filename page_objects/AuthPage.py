from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException
import allure

class AuthPage(BasePage):
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "input[type='submit']")
    SUCCESS = (By.CSS_SELECTOR, "a[href='https://demo-opencart.ru/index.php?route=account/edit']")
    NO_SUCCESS = (By.CSS_SELECTOR, "[class='alert alert-danger alert-dismissible']")
    
    
    @allure.step("Проверка отображения поля Email")
    def check_email(self):
        self._element(self.EMAIL)
        
        
    @allure.step("Проверка отображения поля Пароль")
    def check_password(self):
        self._element(self.PASSWORD)
        
        
    @allure.step("Проверка отображения кнопки продолжить")
    def check_button_submit(self):
        self._element(self.BUTTON_SUBMIT)
        
        
    @allure.step("Заполнение поля Email")
    def input_email(self,email):
        self._element(self.EMAIL).clear()
        self._element(self.EMAIL).send_keys(email)
        
        
    @allure.step("Заполнение поля Пароль")
    def input_password(self,password):
        self._element(self.PASSWORD).clear()
        self._element(self.PASSWORD).send_keys(password)
        
        
    @allure.step("Нажать на кнопку продолжить")
    def click_button_submit(self):
        self._click(self.BUTTON_SUBMIT)
        
        
    @allure.step("Проверка успешной авторизации")
    def check_success(self):
        self._element(self.SUCCESS)
        
    
    @allure.step("Проверка не успешной авторизации")
    def check_no_success(self):
        self._element(self.NO_SUCCESS)
        
        
    
    
    