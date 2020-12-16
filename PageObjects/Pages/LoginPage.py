from selenium import webdriver
from PageObjects.locators import Locators
from selenium.webdriver.common.by import By

class FirstPage():
    def __init__(self,driver):
        self.driver=driver

    def getusername(self,username):
        self.driver.find_element(By.ID, Locators.username_ID).clear()
        self.driver.find_element(By.ID, Locators.username_ID).send_keys(username)

    def getpas(self,password):
        self.driver.find_element(By.ID,Locators.pas_id).clear()
        self.driver.find_element(By.ID,Locators.pas_id).send_keys(password)

    def getlogin(self):
        self.driver.find_element(By.NAME,Locators.login_id).click()



