

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
class create_board:

    board_create_xpath = '//li[@data-test-id="create-board-tile"]'
    board_title_xpath = '//input[@data-test-id="create-board-title-input"]'
    template_button_xpaths = '//div[@id="layer-manager-overlay"]//button'
    type_of_project_xpath = '//section//li'
    submit_but_xpath = '*//button[@data-test-id="create-board-submit-button"]'

    def __init__(self,driver):
        self.driver = driver

    def click_new_board(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.board_create_xpath)))
        self.driver.find_element_by_xpath(self.board_create_xpath).click()

    def create_new_board(self, project_name):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.board_title_xpath)))
        self.driver.find_element_by_xpath(self.board_title_xpath).send_keys(project_name)

    def create_a_board(self, proj_id, proj_type):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.template_button_xpaths)))
        id_list = self.driver.find_elements_by_xpath(self.template_button_xpaths)
        for team_visible in id_list:
            print(team_visible.text)
            if team_visible.text == "Team visible":
                team_visible.click()
                break
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.type_of_project_xpath)))
        name_list = self.driver.find_elements_by_xpath(self.type_of_project_xpath)
        for type_of_project in name_list:
            print(type_of_project.text)
            if type_of_project.text == "Public":
                type_of_project.click()
                break

    def submit_create_board(self):
        self.driver.find_element_by_xpath(self.submit_but_xpath).click()
