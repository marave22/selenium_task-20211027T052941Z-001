# Test N2 
# Remove it from the basket and make sure the basket is empty

from time import sleep
import pytest
from selenium_task.shop.base_page import Base
from selenium_task.shop.shop import Shop

@pytest.mark.usefixtures('set_up')
class Test1(Base):

    def remove_item(self):
        driver = self.driver
        shop = Shop(driver)
        message_cart = shop.message
        assert message_cart == "Your shopping cart is empty", "test failed"

        sleep(5)
        driver.close()
