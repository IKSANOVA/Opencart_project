import os.path

import pytest
from selenium import webdriver
import logging
import datetime
import allure


def pytest_addoption(parser):
    parser.addoption("--url", default="https://demo-opencart.ru")
    parser.addoption("--driver", default="pytest")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption('--ignore-certificate-errors')

@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")
    
    
@pytest.fixture
def browser(request):
    str_driver = request.config.getoption("--driver")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("Test {} started at {}".format(request.node.name, datetime.datetime.now()))
    if str_driver == "Chrome":
        driver = webdriver.Chrome(
            executable_path=os.path.expanduser("C:/driver/chromedriver")
        )
    elif str_driver == "FireFox":
        driver = webdriver.Chrome(
            executable_path=os.path.expanduser("C:/driver/geckodriver")
        )
    elif str_driver == "Opera":
        driver = webdriver.Chrome(
            executable_path=os.path.expanduser("C:/driver/operadriver")
        )
    else:
        raise ValueError(f"Incorrect driver {str_driver}")
    driver.maximize_window()
    driver.log_level = log_level
    driver.logger = logger

    # logger.info("Browser:{}".format(browser, driver.desired_capabilities))
    yield driver

    driver.close()
    logger.info("Test {} finished at {}".format(request.node.name, datetime.datetime.now()))
