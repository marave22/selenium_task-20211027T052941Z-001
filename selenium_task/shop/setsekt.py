# Test N2
# Remove it from the basket and make sure the basket is empty

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

path = 'C:/Users/mariam.avetisyan/Downloads/selenium_task-20211027T052941Z-001/selenium_task/driver/chromedriver.exe'
driver = webdriver.Chrome(executable_path=path)
driver.get("http://automationpractice.com/index.php?id_category=3&controller=category")
driver.maximize_window()

card = driver.find_element_by_css_selector('#center_column > ul > li:nth-child(1) > div > div.right-block')
hover = driver.find_element_by_css_selector('#center_column > ul > li:nth-child(2) > div > div.right-block > '
                                            'div.button-container > a.button.ajax_add_to_cart_button.btn.btn-default '
                                            '> span')
hover = ActionChains(driver).move_to_element(card).move_to_element(hover)
hover.click().perform()

remove_popup = driver.find_element_by_class_name("cross")
driver.implicitly_wait(10)
remove_popup.click()

cart_hover = driver.find_element_by_css_selector('#header > div:nth-child(3) > div > div > div:nth-child(3) > div > a')
hover_cart = ActionChains(driver).move_to_element(cart_hover)
hover_cart.perform()

cart = driver.find_element_by_class_name('shopping_cart')
cart.click()

try:
    alert_warning = driver.find_element_by_class_name('ajax_cart_quantity')
    q = alert_warning.text
    if q == "Your shopping cart is empty.":
        print("success")
except:
  print("In cart exist product")

sleep(5)
driver.close()
