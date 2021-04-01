from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    user_name_id = "user"
    button_login_atlassian_login_id = "login"
    password_id = "password"
    login_button_id = "login-submit"
    logout_action_xpath = '//*[@id="header"]/div[2]/button[contains(@title, "deepan")]/div/span'
    logout_xpath = '//span[contains(text(),"Log out")]'
    logout_final_id = "logout-submit"

    def __init__(self, driver):
        self.driver = driver


    def set_user_name(self, username):
        self.driver.find_element_by_id(self.user_name_id).clear()
        self.driver.find_element_by_id(self.user_name_id).send_keys(username)

    def login_atlassian_acc(self):
        self.driver.find_element_by_id(self.button_login_atlassian_login_id).click()

    def use_password(self, password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def first_submit_button(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def traverse_to_logout(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.logout_action_xpath)))
        self.driver.find_element_by_xpath(self.logout_action_xpath).click()

    def log_out(self):
        self.driver.find_element_by_xpath(self.logout_xpath).click()

    def log_out_final(self):
        self.driver.find_element_by_id(self.logout_final_id).click()

