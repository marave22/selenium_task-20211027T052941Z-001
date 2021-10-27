# Test N1 
# Add an item to the basket and make sure it is in the basket

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

path = 'C:/Users/mariam.avetisyan/Downloads/selenium_task-20211027T052941Z-001/selenium_task/driver/chromedriver.exe'
driver = webdriver.Chrome(executable_path=path)
driver.get("http://automationpractice.com/index.php?id_category=3&controller=category")
driver.maximize_window()



try:
    quantity = driver.find_element_by_class_name()
    q = quantity.text
    if int(q) > 0:
        print("success")
except:
    print("An exception occurred")

sleep(5)
driver.close()
