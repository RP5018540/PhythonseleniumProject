from selenium import webdriver

import pytest
from PageObjects.Pages.LoginPage import FirstPage
from PageObjects.Pages.SearchhotelPage import SecondPage
from PageObjects.Pages.Bookingpage import ThirdPage
from PageObjects.Pages.paymentpage import FourthPage
class Test_adactin():
    @pytest.fixture()
    def setup(self):
        print("Before execution")
        self.driver = webdriver.Chrome(
            executable_path=r"C:\Users\Venkat\PycharmProjects\seleniumpythonframework\driver\chromedriver.exe")
        self.driver.get("http://adactinhotelapp.com/")
        driver = self.driver
        yield
        driver.quit()
        print("After execution")

    def test_login(self,setup):

        F = FirstPage(self.driver)
        username = "Radhika19"
        password = "laksha@19"
        F.getusername(username)
        F.getpas(password)
        F.getlogin()
        assert self.driver.title == "Adactin.com - Search Hotel"


        S=SecondPage(self.driver)
        S.location("Paris")
        S.hotel("Hotel Sunshine")
        S.room("Standard")
        S.roomnos("2")
        S.indate("17/11/2020")
        S.outdate("18/11/2020")
        S.Adult("3")
        S.Child("2")
        S.submit()


        T = ThirdPage(self.driver)
        T.btnclick()
        T.continuebtn()


        F = FourthPage(self.driver)
        F.getfname("Radhika")
        F.getlname("Prabhakaran")
        F.billingaddress("7,ABG,hyuui,lopp-13")
        F.cardno("1234567891234567")
        F.cardtype("AMEX")
        F.expmonth("7")
        F.expyear("2020")
        F.ccv("258")
        F.btnbook()
