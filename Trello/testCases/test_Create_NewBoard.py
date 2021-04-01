import pytest
import time
from pageObjects.Create_NewBoard import create_board
from pageObjects.LoginPage import Login


class Test_001_Create_board:
    base_url = "https://trello.com/login"
    username = "deepanbme@gmail.com"
    password = "Deepan123"
    proj_id = "Team visible"
    proj_type = "Public"

    def test_home_page(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = Login(self.driver)
        self.lp.set_user_name(self.username)
        time.sleep(1)
        self.lp.login_atlassian_acc()
        self.lp.use_password(self.password)
        self.lp.first_submit_button()

        self.cb = create_board(self.driver)
        self.cb.click_new_board()
        self.cb.create_new_board("Demo1")
        self.cb.create_a_board(self.proj_id,self.proj_type)
        self.cb.submit_create_board()


