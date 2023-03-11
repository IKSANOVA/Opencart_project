from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException
import allure

class RegisterPage(BasePage):
    FIRSTNAME = (By.NAME, "firstname")
    LASTNAME = (By.NAME, "lastname")
    EMAIL = (By.NAME, "email")
    TELEPHONE = (By.NAME, "telephone")
    PASS = (By.NAME, "password")
    CONFPASS = (By.NAME, "confirm")
    AGREE = (By.NAME, "agree")
    BUTTON_NEXT = (By.CSS_SELECTOR, "input[type='submit']")
    CONFERM = (By.ID, "content")
    
    
    @allure.step("Успешная регистрация")
    def check_reg_successfully(self):
        self._element(self.CONFERM)
    
    
    @allure.step("Нажать кнопку Продолжить")
    def click_button_next(self):
        self._click(self.BUTTON_NEXT)
    
    
    @allure.step("Установка флажка на согласии")
    def click_agree(self):
        self._click(self.AGREE)
    
    
    @allure.step("Заполнение поля Имя")
    def input_firstname(self,firstname):
        self._element(self.FIRSTNAME).clear()
        self._element(self.FIRSTNAME).send_keys(firstname)
        

    @allure.step("Заполнение поля Фамилия")
    def input_lastname(self, lastname):
        self._element(self.LASTNAME).clear()
        self._element(self.LASTNAME).send_keys(lastname)


    @allure.step("Заполнение поля e-mail")
    def input_email(self, email):
       self._element(self.EMAIL).clear()
       self._element(self.EMAIL).send_keys(email)
        

    @allure.step("Заполнение поля телефон")
    def input_telephon(self, telephon):
        self._element(self.TELEPHONE).clear()
        self._element(self.TELEPHONE).send_keys(telephon)
        
        
    @allure.step("Заполнение поле Пароль")
    def input_passw(self, passw):
        self._element(self.PASS).clear()
        self._element(self.PASS).send_keys(passw)
        
    
    @allure.step("Заполнение поле Подтверждение пароля")
    def input_conf_passw(self, passw):
        self._element(self.CONFPASS).clear()
        self._element(self.CONFPASS).send_keys(passw)


    @allure.step("Проверка элемента Имя")
    def check_firstname(self):
        self._element(self.FIRSTNAME)


    @allure.step("Проверка элемента Фамилия")
    def check_lastname(self):
        self._element(self.LASTNAME)


    @allure.step("Проверка элемента e-mail")
    def check_email(self):
        self._element(self.EMAIL)
        

    @allure.step("Проверка элемента телефон")
    def check_telephon(self):
        self._element(self.TELEPHONE)
