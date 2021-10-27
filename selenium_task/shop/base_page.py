import pytest
from selenium import webdriver


class Base:

    def __init__(self):
        self.driver = None

    @pytest.fixture()
    def set_up(self):
        path = 'C:/Users/mariam.avetisyan/Downloads/selenium_task-20211027T052941Z-001/selenium_task/driver' \
               '/chromedriver.exe '
        driver = webdriver.Chrome(executable_path=path)
        driver.implicitly_wait(10)
        driver.get("http://automationpractice.com/index.php?id_category=3&controller=category")
        driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
