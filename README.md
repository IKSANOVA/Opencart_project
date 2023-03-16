# Автоматизация тестирования приложения OpenCart
Запуск автотестов:
pytest
pytest --driver=Chrome
pytest d:\Python_UI\tests\test_admin.py

pytest --driver=Chrome --alluredir=allure_report
D:\allure-2.18.0\bin\allure.bat serve allure_report



