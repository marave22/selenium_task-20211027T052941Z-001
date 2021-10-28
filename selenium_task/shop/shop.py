from selenium.webdriver import ActionChains

from selenium_task.locators.locators import LocatorsXPath


class Shop:

    def __init__(self, driver):
        self.driver = driver
        self.card = LocatorsXPath.card
        self.hover = LocatorsXPath.hover
        self.add_to_cart = LocatorsXPath.add_to_cart
        self.remove_popup = LocatorsXPath.remove_popup
        self.cart_hover = LocatorsXPath.cart_hover
        self.cart_quantity = LocatorsXPath.cart_quantity
        self.remove_items = LocatorsXPath.remove_items
        self.empty_message = LocatorsXPath.empty_message

    def quantity_cart(self):
        card = self.driver.find_element_by_css_selector(self.card)
        hover = self.driver.find_element_by_css_selector(self.hover)
        hover = ActionChains(self.driver).move_to_element(card).move_to_element(hover)
        hover.click().perform()
        self.driver.implicitly_wait(60)

        remove_popup = self.driver.find_element_by_xpath(self.remove_popup)
        self.driver.implicitly_wait(5)
        remove_popup.click()

        cart_hover = self.driver.find_element_by_xpath(self.cart_hover)
        hover_cart = ActionChains(self.driver).move_to_element(cart_hover)
        hover_cart.perform()

        cart_quantity = self.driver.find_element_by_xpath(self.cart_quantity).text
        return cart_quantity

    def item_remove(self, text):
        card = self.driver.find_element_by_css_selector(self.card)
        hover = self.driver.find_element_by_css_selector(self.hover)
        hover = ActionChains(self.driver).move_to_element(card).move_to_element(hover)
        hover.click().perform()
        self.driver.implicitly_wait(60)

        remove_popup = self.driver.find_element_by_xpath(self.remove_popup)
        self.driver.implicitly_wait(5)
        remove_popup.click()

        cart_hover = self.driver.find_element_by_xpath(self.cart_hover)
        hover_cart = ActionChains(self.driver).move_to_element(cart_hover)
        hover_cart.click().perform()

        remove_items = self.driver.find_element_by_xpath(self.remove_items)
        remove_items.click()
        self.driver.implicitly_wait(60)

        empty_message = self.driver.find_element_by_xpath(self.empty_message).text
        return empty_message
