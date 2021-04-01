import pytest
from selenium import webdriver
import time

from pageObjects.LoginPage import Login

'''
Verify if customer is able to login and log out successfully
'''

class Test_001_Login:

    base_url = "https://trello.com/login"
    username = "deepanbme@gmail.com"
    password = "Deepan123"

    def test_home_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        self.driver.close()

        if actual_title == "Log in to Trello":
            assert True

        else:
            assert False

    def test_home_page(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = Login(self.driver)
        self.lp.set_user_name(self.username)
        time.sleep(1)
        self.lp.login_atlassian_acc()
        self.lp.use_password(self.password)
        self.lp.first_submit_button()
        self.lp.traverse_to_logout()
        actual_title = self.driver.title
        self.lp.log_out()
        self.lp.log_out_final()
        self.driver.close()
        if actual_title == "Boards | Trello":
            print("line 36 ",actual_title)
            assert True
        else:
            assert False

