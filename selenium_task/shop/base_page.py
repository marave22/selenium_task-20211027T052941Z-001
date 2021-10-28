from selenium import webdriver
import pytest


class Base:
    @pytest.fixture()
    def set_up(self):
        path = 'C:/Users/mariam.avetisyan/Downloads/selenium_task-20211027T052941Z-001/selenium_task/driver/chromedriver.exe'
        self.driver = webdriver.Chrome(path)
        self.driver.implicitly_wait(10)
        self.driver.get("http://automationpractice.com/index.php?id_category=3&controller=category")
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()

