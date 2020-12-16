from selenium import webdriver
from selenium.webdriver.support.select import Select
from PageObjects.locators import Locators
from selenium.webdriver.common.by import By

class FourthPage():
    def __init__(self,driver):
        self.driver=driver


    def getfname(self,firstname):
        self.driver.find_element(By.ID, Locators.textbox_fname_id).clear()
        self.driver.find_element(By.ID, Locators.textbox_fname_id).send_keys(firstname)

    def getlname(self,lastname):
        self.driver.find_element(By.ID,Locators.textbox_lname_id).clear()
        self.driver.find_element(By.ID,Locators.textbox_lname_id).send_keys(lastname)

    def billingaddress(self,adrs):
        self.driver.find_element(By.ID,Locators.textbox_address_id).clear()
        self.driver.find_element(By.ID,Locators.textbox_address_id).send_keys(adrs)

    def cardno(self,no):
        self.driver.find_element(By.ID,Locators.textbox_cardno_id).clear()
        self.driver.find_element(By.ID,Locators.textbox_cardno_id).send_keys(no)

    def cardtype(self,value):
        cardtype=self.driver.find_element(By.ID, Locators.select_cardtype_id)
        s = Select(cardtype)
        s.select_by_value(value)

    def expmonth(self,value):
        expmonth=self.driver.find_element(By.ID, Locators.select_expmonth_id)
        s = Select(expmonth)
        s.select_by_value(value)

    def expyear(self,value):
        expyear=self.driver.find_element(By.ID, Locators.select_expyear_id)
        s = Select(expyear)
        s.select_by_value(value)


    def ccv(self,vale):
        self.driver.find_element(By.ID,Locators.textbox_ccv_id).clear()
        self.driver.find_element(By.ID,Locators.textbox_ccv_id).send_keys(vale)

    def btnbook(self):
        self.driver.find_element(By.ID, Locators.btn_book_id).click()



