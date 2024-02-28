from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


driver.maximize_window()
driver.get("https://www.saucedemo.com/")

eleLogin = driver.find_element(By.ID, "user-name")
elePassword = driver.find_element(By.ID, "password")
eleButton = driver.find_element(By.ID, "login-button")

eleLogin.send_keys("standard_user")
elePassword.send_keys("secret_sauce")

eleButton.click()

eleMenu = driver.find_element(By.ID, "react-burger-menu-btn")

eleMenu.cloick()

eleLogout = driver.find_element(By.ID, "logout_sidebar_link")

eleLogout.click()

eleLogin.send_keys("locked_out_user")
elePassword.send_keys("secret_sauce")

eleButton.click()

'''eleAddCart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")

eleAddCart.click()''' # Добавлен товара в корзину


#driver.set_page_load_timeout(30)
# driver.close()
