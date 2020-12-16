import time
from selenium import webdriver
import unittest
from PageObjects.Pages.LoginPage import FirstPage
from PageObjects.Pages.SearchhotelPage import SecondPage
from PageObjects.Pages.Bookingpage import ThirdPage
from PageObjects.Pages.paymentpage import FourthPage
from PageObjects import XLutilities
import openpyxl

class Test_adactin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path=r"C:\Users\Venkat\PycharmProjects\seleniumpythonframework\driver\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
    def test_adactin(self):
        path=r"C:\Users\Venkat\Desktop\Green Tech\Test.xlsx"
        rows=XLutilities.getrowcount(path,'login')
        for r in range (2,rows+1):
            username=XLutilities.readdata(path,'login',r,1)
            password = XLutilities.readdata(path, 'login', r, 2)

            driver = self.driver
            driver.get("http://adactinhotelapp.com/")
            F = FirstPage(driver)
            F.getusername(username)
            F.getpas(password)
            F.getlogin()

            self.assertNotEqual('Adactin.com - Search Hotel',driver.title,"title isnt matching")




        S=SecondPage(driver)
        S.location("Paris")
        S.hotel("Hotel Sunshine")
        S.room("Standard")
        S.roomnos("2")
        S.indate("17/11/2020")
        S.outdate("18/11/2020")
        S.Adult("3")
        S.Child("2")
        S.submit()

        T=ThirdPage(driver)
        T.btnclick()
        T.continuebtn()

        F=FourthPage(driver)
        F.getfname("Radhika")
        F.getlname("Prabhakaran")
        F.billingaddress("7,ABG,hyuui,lopp-13")
        F.cardno("1234567891234567")
        F.cardtype("AMEX")
        F.expmonth("7")
        F.expyear("2020")
        F.ccv("258")
        F.btnbook()

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__=='__main':
    unittest.main()

