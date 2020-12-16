from selenium import webdriver
from selenium.webdriver.support.select import Select

from PageObjects.locators import Locators
from selenium.webdriver.common.by import By

class SecondPage():
    def __init__(self,driver):
        self.driver=driver

    def location(self,value):
        location=self.driver.find_element(By.ID, Locators.location_id)
        s=Select(location)
        s.select_by_value(value)

    def hotel(self,value):
        hotel=self.driver.find_element(By.ID, Locators.hotel_id)
        s = Select(hotel)
        s.select_by_value(value)

    def room(self,value):
        room=self.driver.find_element(By.ID, Locators.roomtype_id)
        s = Select(room)
        s.select_by_value(value)

    def roomnos(self,value):
        roomnos=self.driver.find_element(By.ID, Locators.roomcount_id)
        s = Select(roomnos)
        s.select_by_value(value)

    def indate(self,value):
        self.driver.find_element(By.ID, Locators.chkindate_name).clear()
        self.driver.find_element(By.ID, Locators.chkindate_name).send_keys(value)

    def outdate(self,value):
        self.driver.find_element(By.ID, Locators.chkoutdate).clear()
        self.driver.find_element(By.ID, Locators.chkoutdate).send_keys(value)


    def Adult(self,value):
        Adult=self.driver.find_element(By.ID, Locators.adultperroom_id)
        s = Select(Adult)
        s.select_by_value(value)

    def Child(self,value):
        Child = self.driver.find_element(By.ID, Locators.childperrom)
        s = Select(Child)
        s.select_by_value(value)

    def submit(self):
        self.driver.find_element(By.ID, Locators.submit_id).click()



