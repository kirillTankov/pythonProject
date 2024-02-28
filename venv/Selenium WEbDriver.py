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


#driver.set_page_load_timeout(30)
# driver.close()