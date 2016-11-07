# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from book_entry import BookEntry


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_entry(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd):
        self.open_home_page(wd)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def add_book_entry(self, wd, entry):
        # open add address book entry
        wd.find_element_by_link_text("add new").click()
        # fill address book entry form
        for key, item in entry.parament.items():
            wd.find_element_by_name(key).click()
            wd.find_element_by_name(key).clear()
            wd.find_element_by_name(key).send_keys(item)

        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, success):
        # logout
        self.assertTrue(success)

    def test_test_add_entry(self):
        success = True
        wd = self.wd
        self.login(wd)
        addEntry = BookEntry(firstname="Светлана", middlename="Иларионовна", lastname="Смирнова", work="безработный", address="Не дом и не улица", mobile='8915223344')
        self.add_book_entry(wd, addEntry)
        self.return_to_home_page(wd)
        self.logout(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
