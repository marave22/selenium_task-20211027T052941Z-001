# http://automationpractice.com/index.php?id_category=3&controller=category

# Test N1 
# Add an item to the basket and make sure it is in the basket
# Test N2 
# Remove it from the basket and make sure the basket is empty

from selenium_task.locators.locators import LocatorsXPath
from selenium.webdriver.common.action_chains import ActionChains


class Shop:

    def __init__(self, driver):
        self.driver = driver
        self.card = LocatorsXPath.card
        self.hover = LocatorsXPath.hover
        self.remove_popup = LocatorsXPath.remove_popup
        self.cart_hover = LocatorsXPath.cart_hover
        self.quantity = LocatorsXPath.quantity

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
