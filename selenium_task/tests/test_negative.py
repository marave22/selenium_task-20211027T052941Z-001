# http://automationpractice.com/index.php?id_category=3&controller=category

# Test N1
# Add an item to the basket and make sure it is in the basket
# Test N2
# Remove it from the basket and make sure the basket is empty

import pytest
from time import sleep
from selenium_task.shop.base_page import Base
from selenium_task.shop.shop import Shop


@pytest.mark.usefixtures('set_up')
class TestNegative(Base):
    def test_1_2_negative(self):
        driver = self.driver
        shop = Shop(driver)
        cart_quantity = shop.item_remove(self)
        assert cart_quantity > 0, "positive test failed"
        sleep(5)

        assert "Your shopping cart is full" not in driver.page_source
        sleep(5)
        driver.close()
