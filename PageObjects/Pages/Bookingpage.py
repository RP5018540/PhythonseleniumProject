from selenium import webdriver
from PageObjects.locators import Locators
from selenium.webdriver.common.by import By

class ThirdPage():
    def __init__(self,driver):
        self.driver=driver

    def btnclick(self,):
        self.driver.find_element(By.ID, Locators.radio_btn_id).click()


    def continuebtn(self):
        self.driver.find_element(By.ID,Locators.continue_click_id).click()






