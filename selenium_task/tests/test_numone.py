# Test N1 
# Add an item to the basket and make sure it is in the basket

# Test N2
# Remove it from the basket and make sure the basket is empty

from time import sleep
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium_task.shop.base_page import Base
from selenium_task.shop.shop import Shop

@pytest.mark.usefixtures('set_up')
class Test1(Base, Shop):

    def add_cart(self):
        card = self.driver.find_element_by_css_selector(self.card)
        hover = self.driver.find_element_by_css_selector(self.hover)
        hover = ActionChains(self.driver).move_to_element(card).move_to_element(hover)
        hover.click().perform()
        self.driver.implicitly_wait(5)

        remove_popup = self.driver.find_element_by_class_name(self.remove_popup)
        self.driver.implicitly_wait(5)
        remove_popup.click()

        cart_hover = self.driver.find_element_by_css_selector(self.cart_hover)
        hover_cart = ActionChains(self.driver).move_to_element(cart_hover)
        hover_cart.perform()


    def cart_quantity(self, text):
        item_quantity = self.driver.find_element_by_class_name(self.quantity).text
        item_quantity.send_keys(text)

    
    def remove_cart(self, text):
        cart_hover = self.driver.find_element_by_css_selector(self.cart_hover)
        cart_hover.click()

        remove_item = self.driver.find_element_by_xpath(self.remove_item)
        remove_item.click()

        message = self.driver.find_element_by_css_selector(self.message).text
        message.send_keys(text)

    def check_cart(self):
        driver = self.driver
        shop = Shop(driver)
        cart_quantity = shop.cart_quantity
        cart_quantity_out = 1
        assert cart_quantity == cart_quantity_out, "positive test failed"

        sleep(5)
        driver.close()