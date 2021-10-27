# http://automationpractice.com/index.php?id_category=3&controller=category

# Test N1 
# Add an item to the basket and make sure it is in the basket
# Test N2 
# Remove it from the basket and make sure the basket is empty

from locators import LocatorsXPath
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class Shop:

    def __init__(self, driver):
        self.driver = driver
        self.card = LocatorsXPath.card
        self.hover = LocatorsXPath.hover
        self.remove_popup = LocatorsXPath.remove_popup
        self.cart_hover = LocatorsXPath.cart_hover
        self.quantity = LocatorsXPath.quantity
        self.remove_item = LocatorsXPath.remove_item
        self.message = LocatorsXPath.message

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

        item_quantity = self.driver.find_element_by_class_name(self.quantity).text

        cart_hover = self.driver.find_element_by_css_selector(self.cart_hover)

        remove_item = self.driver.find_element_by_xpath(self.remove_item)
        remove_item.click()

        message = self.driver.find_element_by_css_selector(self.message).text

    def check_cart(self):
        driver = self.driver
        cart_quantity = self.item_quantity
        cart_quantity_out = 1
        assert cart_quantity == cart_quantity_out, "positive test failed"

        sleep(5)
        driver.close()

    def remove_item(self):
        driver = self.driver
        message_cart = self.message
        assert message_cart == "Your shopping cart is empty", "test failed"

        sleep(5)
        driver.close()