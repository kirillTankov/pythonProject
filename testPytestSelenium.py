import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class AuthTest:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()

    def login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")
        eleLogin = self.driver.find_element(By.ID, "user-name")
        elePassword = self.driver.find_element(By.ID, "password")
        eleButton = self.driver.find_element(By.ID, "login-button")
        eleLogin.send_keys(username)
        elePassword.send_keys(password)
        eleButton.click()
        return self.driver.current_url

    def logout(self):
        eleMenu = self.driver.find_element(By.ID, "react-burger-menu-btn")
        eleMenu.click()
        eleLogout = self.driver.find_element(By.CSS_SELECTOR, "#logout_sidebar_link")
        eleLogout.click()

    def clear_fields(self):
        eleLogin = self.driver.find_element(By.ID, "user-name")
        elePassword = self.driver.find_element(By.ID, "password")
        eleLogin.clear()
        elePassword.clear()

@pytest.fixture
def auth_test():
    test = AuthTest()
    yield test
    test.driver.quit()

# Тестирование авторизации с разными пользователями
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce")
])
def test_login(auth_test, username, password):
    url = auth_test.login(username, password)
    if "inventory" in url:
        print(f"Пользователь {username} успешно вошел.")
        assert True
    else:
        print(f"Ошибка входа для пользователя {username}.")
        assert False
    auth_test.logout()
    auth_test.clear_fields()
