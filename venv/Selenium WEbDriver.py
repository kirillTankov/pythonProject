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
        # Проверяем успешность входа
        if "inventory" in self.driver.current_url:
            print(f"Пользователь {username} успешно вошел.")
            return True
        else:
            print(f"Ошибка входа для пользователя {username}.")
            return False

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

auth_test = AuthTest()

# Примеры тестирования каждого пользователя
users = [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce")
]

for user in users:
    success = auth_test.login(user[0], user[1])
    if not success:
        auth_test.clear_fields()  # Очищаем поля ввода
